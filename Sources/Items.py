""" Text adventure game
    @year  = 2022
"""
__author__ = "TeamCodeIt"

import random


class Weapon:
    def __init__(self):
        raise NotImplementedError("Dop not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Pocket_knife(Weapon):
    def __init__(self):
        self.name = "Pocket_knife"
        self.description = "Baisic tool, made in China"
        self.damage = 5
        self.value = 0


class Cutter_knife(Weapon):
    def __init__(self):
        self.name = "Cutter_knife"
        self.description = "A utility knife with some rust. " \
                           "The blade breaks easily"
        self.damage = 10
        self.value = 0


class Slingshot(Weapon):
    def __init__(self):
        self.name = "Slingshot"
        self.description = "The probability of enemy increases by 10%" \
                           " but still its firearm. "
        self.damage = 12
        self.value = 90


class Coin(Weapon):
    def __init__(self):
        self.name = "Coin"
        self.description = "Bullet of Slingshot"
        self.damage = 1
        self.value = 1


class Cardboard_Box(Weapon):
    def __init__(self):
        self.name = "Cardboard_Box"
        self.description = "Ignore any damage."
        self.damage = 0
        self.value = 35
        
        
class MOP(Weapon):
    def __init__(self):
        self.name = "MOP"
        self.description = "Big Swing, Critical Damage."
        self.damage = 7
        self.value = 70
        
     
class Fluorescent_Light(Weapon):
    def __init__(self):
        self.name = "Fluorescent_Light"
        self.description = "Disposable weapon, That's lot of damage."
        self.damage = 50
        self.value = 300
        
        
class Scissor(Weapon):
    def __init__(self):
        self.name = "Scissor"
        self.description = "5% chance to debuff -1 HP when you hit enemy."
        self.damage = 3
        self.value = 30
        
        
class Wallet(Weapon):
    def __init__(self):
        self.name = "Wallet"
        self.description = "When you hold this you can get 10% more Gold."
        self.damage = 0
        self.value = 20
        
        
class KEY(Weapon):
    def __init__(self):
        self.name = "Cardboard_Box"
        self.description = "Ignore any damage."
        self.random = 0.01
        self.value = 50
        r = random.random()
        if r <= self.random :
            self.damage = 100
        else:
            self.damage = 1
            
            
class Butain(Weapon):
    def __init__(self):
        self.name = "Butain"
        self.description = "When you throw this canister, damaging enemy 5% of max hp in 5 turns."
        self.damage = """damaginf enemy 5% of max HP in 5 turns"""
        self.value = 30



class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class Powerade(Consumable):
    def __init__(self):
        self.name = "Powerade"
        self.healing_value = 5
        self.value = 5


class Cola(Consumable):
    def __init__(self):
        self.name = "Cola"
        self.healing_value = 50
        self.value = 5
        """Recover 10% of your max hp in 5 turns"""
        
        
class Energ_drink(Consumable):
    def __init__(self):
        self.name = "Energ_drink"
        self.damage = 5% """damage increases by 5%"""
        self.value = 7

        
class TWO_Soju(Consumable):
    def __init__(self):
        self.name = "TWO_Soju"
        self.healing_value = 10 """make your hp 1 but you do not get any damage"""
        self.value = 15
        
        
class Stick_Icecream(Consumable):
    def __init__(self):
        self.name = "Stick_Icecream"
        self.healing_value = """defense increases %5"""
        self.value = 5
        
        
class Corn_Icecream(Consumable):
    def __init__(self):
        self.name = "Corn_Icecream"
        self.healing_value = 10 """evasion increases 5%"""
        self.value = 7
        
        
class Potato_Chip(Consumable):
    def __init__(self):
        self.name = "Potato_Chip"
        self.healing_value = 10 """evasion increases 10%"""
        self.value = 5
        
        
class Lollipop(Consumable):
    def __init__(self):
        self.name = "Lollipop"
        self.healing_value = 10 """max HP and defanse increases 1"""
        self.value = 5
        
        
class Small_Chocolate(Consumable):
    def __init__(self):
        self.name = "Small_Chocolate"
        self.healing_value = 10 """increases 1 ATK damage in 1 turn """
        self.value = 5
        
        
class Medium_Chocolate(Consumable):
    def __init__(self):
        self.name = "Medium_Chocolate"
        self.healing_value = 10 """increases 2 ATK damage in 2 turns"""
        self.value = 7
        
        
class Big_Chocolate(Consumable):
    def __init__(self):
        self.name = "Big_Chocolate"
        self.healing_value = 10 """increases 3 ATK damage in 3 turns"""
        self.value = 9
        
        
class Stockings(Consumable):
    def __init__(self):
        self.name = "Stockings"
        self.healing_value = 10 """increases evasion 10%"""
        self.value = 10
        
        
class Plastic_Bag(Consumable):
    def __init__(self):
        self.name = "Plastic_Bag"
        self.healing_value = 10 """increases Bag Size 1"""
        self.value = 15
