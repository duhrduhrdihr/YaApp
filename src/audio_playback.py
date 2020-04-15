import simpleaudio as sa
from os.path import join, relpath
from os import listdir
from random import choice


YAAAP_ROOT = relpath('audio')


def play_audio(yaaap):

    wave_obj = sa.WaveObject.from_wave_file(yaaap)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def pick_random_yaaap():
    files = listdir(YAAAP_ROOT)
    picked_yaaap = choice(files)

    return join(YAAAP_ROOT, picked_yaaap)


yaaap = pick_random_yaaap()
play_audio(yaaap)
