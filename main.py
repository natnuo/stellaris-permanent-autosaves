from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import shutil

directory = input("Save directory to watch: ")
tmp_folder = directory + "\\tmp"

class Handler(FileSystemEventHandler):
  def on_created(self, event):
    file_name = event.src_path.split("\\")[-1]
    if (file_name[:8] == "autosave"):
      try: os.mkdir(tmp_folder)
      except: pass

      shutil.copy(event.src_path, tmp_folder)
      shutil.move(f"{tmp_folder}\\{file_name}", f"{directory}\\{file_name[9::]}")

      print("[SAVED]", file_name[9::])

event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, path=directory, recursive=False)
observer.start()

input('press Enter to quit\n')

observer.stop()