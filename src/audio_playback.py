import simpleaudio as sa


yaaap_file = ".\\audio\\01.wav"


def play_audio(yaaap):

    wave_obj = sa.WaveObject.from_wave_file(yaaap)
    play_obj = wave_obj.play()
    play_obj.wait_done()


# play_audio(yaaap_file)
