from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
from shutil import copyfile


class MyHandler(FileSystemEventHandler):
    """ Handler class to handle event """

    i = 1
    def __init__(self):
        self.old_files_to_track = os.listdir("/home/jaimedgp/Documents/track")

    def on_modified(self, event):
        """ act when modified is detected """

        for filename in os.listdir(folder_to_track):
            print(filename)
            if filename not in self.old_files_to_track:
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/" + filename


                if os.path.isfile(src):
                    copyfile(src, new_destination)
                if os.path.isdir(src):
                    os.mkdir(new_destination)

        self.old_files_to_track = os.listdir("/home/jaimedgp/Documents/track")


folder_to_track = "/home/jaimedgp/Documents/track"
folder_destination = "/home/jaimedgp/Documents/destination"
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
