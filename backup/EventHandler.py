from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
from shutil import copyfile


class MyHandler(FileSystemEventHandler):
    """ Handler class to handle event """

    i = 1
    def on_modified(self, event):
        """ act when modified is detected """

        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            copyfile(src, new_destination)


folder_to_track = "/media/jaimedgp/Archivo"
folder_destination = "/media/jaimedgp/Archivo - Backup"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
