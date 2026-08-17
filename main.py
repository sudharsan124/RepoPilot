import os
import subprocess
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class RepoPilotHandler(FileSystemEventHandler):

    def should_ignore(self, path):
        path = os.path.abspath(path)
        git_folder = os.path.abspath(".git")

        return path.startswith(git_folder)

    def process_change(self, path):

        if self.should_ignore(path):
            return

        print(f"Change detected: {path}")

        try:
            # Get the GitHub remote repository
            remote = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                capture_output=True,
                text=True,
                check=False
            )

            # Stop if no remote repository is configured
            if remote.returncode != 0:
                print("No GitHub remote found. Push cancelled.")
                return

            remote_url = remote.stdout.strip()

            # Safety check: never automatically push to RepoPilot itself
            if "sudharsan124/RepoPilot" in remote_url:
                print("Safety check: RepoPilot repository detected.")
                print("Automatic push cancelled.")
                return

            # Stage changed files
            subprocess.run(
                ["git", "add", "."],
                check=True
            )

            # Check whether there are staged changes
            result = subprocess.run(
                ["git", "diff", "--cached", "--quiet"],
                check=False
            )

            if result.returncode == 0:
                return

            # Create commit
            subprocess.run(
                [
                    "git",
                    "commit",
                    "-m",
                    f"RepoPilot: Updated {os.path.basename(path)}"
                ],
                check=True
            )

            # Push changes
            subprocess.run(
                ["git", "push", "origin", "main"],
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


observer = Observer()

event_handler = RepoPilotHandler()

observer.schedule(
    event_handler,
    ".",
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