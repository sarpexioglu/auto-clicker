import time
import threading

from pynput import mouse
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 0.01
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)


mouse = Controller()
Click_thread = ClickMouse(delay, button)
Click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if Click_thread.running:
            Click_thread.stop_clicking()
        else:
            Click_thread.start_clicking()
    elif key == exit_key:
        Click_thread.exit()
        Listener.stop()


with Listener(on_press=on_press) as Listener:
    Listener.join()
