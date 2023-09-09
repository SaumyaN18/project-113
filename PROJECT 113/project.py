import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir = "C:/Users/Saumya Narsang/Downloads"
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'hiiiiiiiiiiiiiiiiiiiiii,{event.src_path}has been created')
    def on_deleted(self, event):
        print(f'hiiiiiiiiiiiiiiiiiiiiii,{event.src_path}has been deleted')
    def on_modified(self, event):
        print(f'hiiiiiiiiiiiiiiiiiiiiii,{event.src_path}has been modified')
    def on_moved(self, event):
        print(f'hiiiiiiiiiiiiiiiiiiiiii,{event.src_path}has been moved')
eventhandler = FileEventHandler()
observer = Observer()
observer.schedule(eventhandler,from_dir,recursive = True)
observer.start()
try:
    while True:
        time.sleep(2)
        print('Running')
except KeyboardInterrupt:
    print('Stop')
    observer.stop()