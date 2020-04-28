from tkinter import *
from tkinter import ttk

from audio_playback import play_yaaap


root = Tk()
root.title("YaApp")

mainframe = ttk.Frame(root, padding="75 12 75 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Yaaap", command=play_yaaap).grid(column=1)
root.mainloop()
