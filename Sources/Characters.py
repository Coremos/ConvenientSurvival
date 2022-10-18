""" Text adventure game
    @year  = 2022
"""
__author__ = "TeamCodeIt"

import Items


class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw Non Playable Character objects.")

    def __str__(self):
        return self.name


class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.gold = 100
        self.inventory = [Items.CrustyBread(),
                          Items.CrustyBread(),
                          Items.CrustyBread(),
                          Items.HealingPotion(),
                          Items.HealingPotion()]