""" Text adventure game
    @year  = 2022
"""
__author__ = "TeamCodeIt"

import Items
import World
import random


class Player:
    def __init__(self):
        self.inventory = [Items.Rock(),
                          Items.Dagger(),
                          Items.CrustyBread()]

        self.x = World.start_tile_location[0]
        self.y = World.start_tile_location[1]
        self.hp = 10
        self.defense = 1
        self.evasion = 0.90
        self.gold = 100
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print("*" + str(item))
        print("*Gold : {}".format(self.gold))
        best_weapon = self.most_powerful_weapon()
        print("Your best weapon is your {}".format(best_weapon))

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None

        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = World.tile_at(self.x, self.y)
        enemy = room.enemy
        defense = best_weapon.damage - enemy.defense
        print("You can use {} against!".format(best_weapon.name, enemy.name))
        r = random.random()
        if r < enemy.evasion :
            print("The player gave the " + str(enemy.name) + str(defense) + " damage!")
            enemy.hp -= defense
        else:
            print("The " + str(enemy.name) + "avoided damage.")
        if  self.hp <= 0:
            print("The" + str(enemy.name) + " is dead.")
        else:
            if self.hp <= 0:
                print("The " + str(enemy.name) + " is dead.")
            else :
                print("The" + str(enemy.name) + " now have a physical strength of " + str(enemy.hp))
        print("-----------------")

    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item, Items.Consumable)]
        if not consumables:
            print("You don't have any items to heal you!")
            return

        for i, item in enumerate(consumables,1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Invalid Choice, try again.")

    def trade(self):
        room = World.tile_at(self.x, self.y)
        room.check_if_trade(self)