import simpleaudio as sa
from os import path
from os import listdir
from random import choice

import sys


bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
YAAAP_ROOT = path.join(bundle_dir, 'audio')


def play_audio(yaaap):

    wave_obj = sa.WaveObject.from_wave_file(yaaap)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def pick_random_yaaap():
    files = listdir(YAAAP_ROOT)
    picked_yaaap = choice(files)

    return path.join(YAAAP_ROOT, picked_yaaap)


def play_yaaap():
    yaaap = pick_random_yaaap()
    play_audio(yaaap)
