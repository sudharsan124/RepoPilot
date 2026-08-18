import os
import subprocess
import time
from urllib.parse import urlparse

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


PROTECTED_REPOSITORY = "sudharsan124/RepoPilot"


class RepoPilotHandler(FileSystemEventHandler):

    def __init__(self, repo_root):
        self.repo_root = repo_root

    def should_ignore(self, path):
        path = os.path.abspath(path)
        git_folder = os.path.join(self.repo_root, ".git")

        try:
            return os.path.commonpath([path, git_folder]) == git_folder
        except ValueError:
            return False

    def is_protected_repository(self, remote_url):
        if remote_url.startswith("https://github.com/"):
            parsed = urlparse(remote_url)
            repository = parsed.path.strip("/")
        elif remote_url.startswith("git@github.com:"):
            repository = remote_url.split(":", 1)[1].strip("/")
        else:
            return False

        if repository.endswith(".git"):
            repository = repository[:-4]

        return repository.lower() == PROTECTED_REPOSITORY.lower()

    def process_change(self, path):

        if self.should_ignore(path):
            return

        print(f"Change detected: {path}")

        try:
            remote = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                check=False
            )

            if remote.returncode != 0:
                print("No GitHub remote found. Push cancelled.")
                return

            remote_url = remote.stdout.strip()

            print(f"Repository: {remote_url}")

            if self.is_protected_repository(remote_url):
                print("Safety check: RepoPilot repository detected.")
                print("Automatic push cancelled.")
                return

            subprocess.run(
                ["git", "add", "."],
                cwd=self.repo_root,
                check=True
            )

            result = subprocess.run(
                ["git", "diff", "--cached", "--quiet"],
                cwd=self.repo_root,
                check=False
            )

            if result.returncode == 0:
                return

            filename = os.path.basename(path)

            subprocess.run(
                [
                    "git",
                    "commit",
                    "-m",
                    f"RepoPilot: Updated {filename}"
                ],
                cwd=self.repo_root,
                check=True
            )

            subprocess.run(
                ["git", "push", "origin", "main"],
                cwd=self.repo_root,
                check=True
            )

            print("Successfully pushed to GitHub!")

        except subprocess.CalledProcessError as error:
            print(f"Git operation failed: {error}")

    def on_created(self, event):
        if not event.is_directory:
            self.process_change(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.process_change(event.src_path)


def get_repository_root():
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False
    )

    if result.returncode != 0:
        return None

    return os.path.abspath(result.stdout.strip())


repo_root = get_repository_root()

if repo_root is None:
    print("Error: RepoPilot must be run inside a Git repository.")
    raise SystemExit(1)

print(f"Repository detected: {repo_root}")

observer = Observer()

event_handler = RepoPilotHandler(repo_root)

observer.schedule(
    event_handler,
    repo_root,
    recursive=True
)

observer.start()

print("RepoPilot is watching for files...")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()