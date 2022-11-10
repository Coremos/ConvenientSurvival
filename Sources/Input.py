from enum import Enum, auto
import keyboard


class KeyType(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    A = auto()
    B = auto()


keyCodes = {}
keyStates = {}
keyDown = {}


def bind_key():
    keyCodes[KeyType.UP] = 72
    keyCodes[KeyType.DOWN] = 80
    keyCodes[KeyType.LEFT] = 75
    keyCodes[KeyType.RIGHT] = 77
    keyCodes[KeyType.A] = 44
    keyCodes[KeyType.B] = 45


def initialize_key():
    bind_key()
    for keyCode in KeyType:
        keyStates[keyCode] = False
        keyDown[keyCode] = False


def update_input():
    for keyCode in KeyType:
        keyDown[keyCode] = False
        if (keyboard.is_pressed(keyCodes[keyCode])):
            if (not keyStates[keyCode]):
                keyDown[keyCode] = True
            keyStates[keyCode] = True
        else:
            keyStates[keyCode] = False


def test_input():
    initialize_key()
    while True:
        update_input()
        for i in KeyType:
            if (keyDown[i]):
                print(i)


def find_key():
    while True:
        for number in range(0, 200):
            if (keyboard.is_pressed(number)):
                print(number)
