""" Text adventure game
    @year  = 2022
"""
__author__ = "TeamCodeIt"

import os
import World
from Input import KeyType
import Input
from Player import Player
from collections import OrderedDict

# def logic():
# Input


def rendering(player):
    map = World.get_map()
    for y in range(0, len(map)):
        for x in range(0, len(map[0])):
            if (x == player.x and y == player.y):
                print('@', end='')
            else:
                print(get_tile_text(map[y][x]), end='')
        print()


def get_tile_text(tile):
    if isinstance(tile, World.EnemyTile):
        return 'E'
    elif isinstance(tile, World.StartTile):
        return 'S'
    elif isinstance(tile, World.TraderTile):
        return 'T'
    elif isinstance(tile, World.FindGoldTile):
        return 'G'
    elif isinstance(tile, World.VictoryTile):
        return 'V'
    else:
        return ' '


def input(room: World.MapTile, player: Player):
    while True:
        Input.update_input()
        if player.inventory:
            if Input.keyDown[KeyType.B]:
                player.print_inventory()
                return
        if (isinstance(room, World.TraderTile)):
            if (Input.keyDown[KeyType.A]):
                player.trade()
                return
        if (isinstance(room, World.EnemyTile) and room.enemy.is_alive()):
            if (Input.keyDown[KeyType.A]):
                player.attack()
                return
        else:
            if (Input.keyDown[KeyType.UP]):
                if World.tile_at(room.x, room.y - 1):
                    player.move_north()
                    return
            if (Input.keyDown[KeyType.DOWN]):
                if World.tile_at(room.x, room.y + 1):
                    player.move_south()
                    return
            if (Input.keyDown[KeyType.LEFT]):
                if World.tile_at(room.x - 1, room.y):
                    player.move_west()
                    return
            if (Input.keyDown[KeyType.RIGHT]):
                if World.tile_at(room.x + 1, room.y):
                    player.move_east()
                    return


def initialize():
    Input.initialize_key()


def play():
    initialize()
    print()
    print()
    print("Escape from Cave Terror!")
    World.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        print()
        room = World.tile_at(player.x, player.y)
        rendering(player)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            #choose_action(room, player)
            input(room, player)
        elif not player.is_alive():
            print("Your journey has come to an early end! ")


def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Print inventory")
    if isinstance(room, World.TraderTile):
        action_adder(actions, 't', player.trade, "Trade")
    if isinstance(room, World.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
    else:
        if World.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go North")
        if World.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "Go South")
        if World.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go East")
        if World.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go West")
        if player.hp < 100:
            action_adder(actions, 'h', player.heal, "Heal")

    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{} : {}".format(hotkey, name))


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")


play()
