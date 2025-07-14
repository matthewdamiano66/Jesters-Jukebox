import random

from PyQt5 import QtWidgets
from playsound3 import playsound

def audio_library():
    print("Hello")
    repo=[
        "/Users/matt/Desktop/Jesters Jukebox/Jesters Jukebox/sounds/lounging/lofi_beat.mp3",
        "/Users/matt/Desktop/Jesters Jukebox/Jesters Jukebox/sounds/lounging/lofi_beat2.mp3"

    ]
    csong=random.choice(repo)
    print(str(csong))
    mp = playsound(csong)

def gui():
    print("gui")

    def button_actions():
        print("I am a button")


    button_actions()

def main():
    audio_library()
    gui()


if __name__ == "__main__":
    main()
