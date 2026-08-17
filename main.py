from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time


class RepoPilotHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return

        print(f"New file detected: {event.src_path}")

        try:
            # Add the new file
            subprocess.run(["git", "add", "."], check=True)

            # Commit
            subprocess.run(
                ["git", "commit", "-m", f"RepoPilot: Added {event.src_path}"],
                check=True
            )

            # Push to GitHub
            subprocess.run(
                ["git", "push", "origin", "main"],
                check=True
            )

            print("Successfully pushed to GitHub!")

        except subprocess.CalledProcessError as error:
            print(f"Git operation failed: {error}")


observer = Observer()

path = "."

event_handler = RepoPilotHandler()
observer.schedule(event_handler, path, recursive=True)

observer.start()

print("RepoPilot is watching for files...")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()