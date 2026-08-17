from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os


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
            subprocess.run(["git", "add", "."], check=True)

            result = subprocess.run(
                ["git", "diff", "--cached", "--quiet"]
            )

            if result.returncode == 0:
                return

            subprocess.run(
                [
                    "git",
                    "commit",
                    "-m",
                    f"RepoPilot: Updated {os.path.basename(path)}"
                ],
                check=True
            )

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