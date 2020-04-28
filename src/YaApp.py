from tkinter import *
from tkinter import ttk
from concurrent import futures
from os import path

from audio_playback import play_yaaap


tpe = futures.ThreadPoolExecutor()

bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
RESOURCES_ROOT = path.join(bundle_dir, 'resources')


def on_button():
    tpe.submit(play_yaaap)


root = Tk()
root.title("YaApp")
root.iconbitmap(path.join(RESOURCES_ROOT, "yaaap_icon.ico"))

mainframe = ttk.Frame(root, padding="75 12 75 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Yaaap playblack is handled on a separate thread, so the GUI doesn't freeze
ttk.Button(mainframe, text="Yaaap", command=on_button).grid(column=1)
root.mainloop()
