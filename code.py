import time
import board
import touchio
from adafruit_circuitplayground import cp
from adafruit_circuitplayground.bluefruit import cpb
import time

def note(name):
    PITCHES = "c,c#,d,d#,e,f,f#,g,g#,a,a#,b".split(",")
    octave = int(name[-1])
    pitch = PITCHES.index(name[:-1].lower())
    return 220 * 2 ** ((octave - 1) + (pitch - 6) / 12)

cpb.pixels.brightness = 0.05

cpb.detect_taps = 2
pixel_number = 0

play_open = False
min_open_light = 4
while True:
    if cp.switch:
        #cpb.pixels.fill((255, 0, 0))
        print("Light level:", cpb.light, "play_open:", play_open)
        if cpb.tapped and cpb.light < min_open_light:
            print("Tap detected!")
            #cp.play_file("audio/tuktuk.wav")
            cp.play_tone(note("g2"), 0.6)
            cp.play_tone(note("e2"), 0.4)
            cp.play_tone(note("a2"), 0.4)
            cp.play_tone(note("g2"), 0.3)
            time.sleep(0.05)
            cp.play_tone(note("g2"), 0.3)
            time.sleep(0.05)
            cp.play_tone(note("e2"), 0.4)
            cpb.pixels.fill((0, 0, 0))
            cpb.pixels[pixel_number] = (0, 0, 50)
            pixel_number += 1
            if pixel_number >= 10:
                pixel_number = 0
        if cpb.light >= min_open_light: #box is open
            if play_open: #box just opened
                print("boker tov")
                cp.play_tone(note("c2"), 0.35)
                cp.play_tone(note("c2"), 0.35)
                cp.play_tone(note("d2"), 0.35)
                cp.play_tone(note("e2"), 0.35)
                cp.play_tone(note("g2"), 0.55)
                cp.play_tone(note("c2"), 0.45)
                cp.play_tone(note("a2"), 0.35)
                cp.play_tone(note("a2"), 0.35)
                cp.play_tone(note("b2"), 0.35)
                cp.play_tone(note("b2"), 0.35)
                cp.play_tone(note("c3"), 0.6)
                time.sleep(0.05)
                cp.play_tone(note("c3"), 0.35)
                cp.play_tone(note("c3"), 0.35)
                cp.play_tone(note("b2"), 0.35)
                cp.play_tone(note("a2"), 0.35)
                cp.play_tone(note("g2"), 0.55)
                cp.play_tone(note("e2"), 0.35)
                cp.play_tone(note("g2"), 0.40)
                cp.play_tone(note("f2"), 0.35)
                cp.play_tone(note("e2"), 0.35)
                cp.play_tone(note("d2"), 0.35)
                cp.play_tone(note("c2"), 0.55)
                cpb.pixels.fill((0, 0, 255))
                play_open = False
        else:
            play_open = True
            #cpb.pixels.fill((0, 0, 0))
    time.sleep(1)

