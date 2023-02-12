import math
import pygame as pg
import numpy as np

pg.init()
pg.mixer.init()

muted = False

def set_muted(mute):
    global muted
    muted = mute

def calc_freq(val):
    val += 147
    freq_ref = 440
    n = 12 * math.log2(val / freq_ref)
    freq = freq_ref * math.pow(2, n/12)

    return freq

def synthesizer(freq, dur=0.1, sample_rate=44100):
    frames = int(dur * sample_rate)
    arr = np.cos(2 * np.pi * freq * np.linspace(0, dur, frames))
    sound = np.asarray([32767 * arr] * 2).T.astype(np.int16)
    sound = pg.sndarray.make_sound(sound.copy())
    
    return sound

def play_note(val):
    if muted:
        return
    freq = calc_freq(val)
    sound = synthesizer(freq)
    sound.play()