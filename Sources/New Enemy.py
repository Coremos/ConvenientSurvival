class Enemy:
    def __init__(self):
        raise NotImplementedError("DO not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0
        
    def doAttack(self):
        print(str(self.name) + "�� �Ʊ����� " + str(self.attack) + "��ŭ �����ߴ�!")
        print("-----------------")

    def hit(self, damage):
        print("�Ʊ���" + str(self.name) + "���� " + str(damage) + "�� �������� �־���!")
        if  self.hp <= 0:
            print(str(self.name) + "�� �̹� ��ü�̴�.....")
        else:
            self.hp -= damage
            if self.hp <= 0:
                print(str(self.name) + "�� �׾���!")
            else :
                print("����" + str(self.name) + "�� ü���� " + str(self.hp) + "�̴�.")
        print("-----------------")

class Boss:
    def __init__(self):
        raise NotImplementedError("DO not create raw Boss objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

        def doAttack(self):
        print(str(self.name) + "�� �Ʊ����� " + str(self.attack) + "��ŭ �����ߴ�!")
        print("-----------------")

    def hit(self, damage):
        print("�Ʊ���" + str(self.name) + "���� " + str(damage) + "�� �������� �־���!")
        if  self.hp <= 0:
            print(str(self.name) + "�� �̹� ��ü�̴�.....")
        else:
            self.hp -= damage
            if self.hp <= 0:
                print(str(self.name) + "�� �׾���!")
            else :
                print("����" + str(self.name) + "�� ü���� " + str(self.hp) + "�̴�.")
        print("-----------------")

class Zombie(Enemy):
    def __init__(self):
        self.name = "Zobie"
        self.hp = 15
        self.damage = 3
        self.defense = 5
        self.gold = 50
        self.evasion = 1

class Skeleton(Enemy):
    def __init__(self):
        self.name = "Skeleton"
        self.hp = 10
        self.damage = 5
        self.defense = 3
        self.gold = 100
        self.evasion = 1

class Ghost(Enemy):
    def __init__(self):
        self.name = "Ghost"
        self.hp = 10
        self.damage = 7
        self.defense = 1
        self.gold = 150
        self.evasion = 5

class Golem(Enemy):
    def __init__(self):
        self.name = "Golem"
        self.hp = 50
        self.damage = 1
        self.defense = 30
        self.gold = 200
        self.evasion = 0.5

class Hobgoblin(Boss):
    def __init__(self):
        self.name = "Hobgoblin"
        self.hp = 100
        self.damage = 30
        self.defense = 15
        self.gold = 300
        self.evasion = 2

class Dragon(Boss):
    def __init__(self):
        self.name = "Dragon"
        self.hp = 150
        self.damage = 30
        self.defense = 30
        self.gold = 300
        self.evasion = 1.5

zombie = Zombie()
zombie.hit(15)

