from microbit import *
import music

while True:

    # Tlačítko A
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        music.play(music.BA_DING)

    # Tlačítko B
    elif button_b.is_pressed():
        display.show(Image.SAD)
        music.play(music.WAWAWAWAA)

    # Zatřesení micro:bitem
    if accelerometer.was_gesture("shake"):
        display.scroll("AHOJ")

    # Zobrazení teploty při otočení nahoru
    if accelerometer.was_gesture("up"):
        teplota = temperature()
        display.scroll(str(teplota))

    sleep(100)
