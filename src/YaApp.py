from tkinter import *
from tkinter import ttk
from concurrent import futures

from audio_playback import play_yaaap


tpe = futures.ThreadPoolExecutor()


def on_button():
    tpe.submit(play_yaaap)


root = Tk()
root.title("YaApp")

mainframe = ttk.Frame(root, padding="75 12 75 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Yaaap playblack is handled on a separate thread, so the GUI doesn't freeze
ttk.Button(mainframe, text="Yaaap", command=on_button).grid(column=1)
root.mainloop()
