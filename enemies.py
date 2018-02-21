'''Create a dictionary of enemies.
'''
import physical_parameters as physpara


class Enemy:
    def __init__(self):
        pass


class Grineer(Enemy):
    def __init__(self):
        pass


class GrineerLancer(Grineer):
    def __init__(self, level):
        self.name = 'Grineer Lancer'
        self.health = physpara.Health(100, 1, level, 'cloned flesh')
        self.shield = physpara.Shield()
        self.armor = physpara.Armor(100, 1, level, 'ferrite')
        self.level = level


class EliteLancer(Grineer):
    def __init__(self, level):
        self.name = 'Grineer Lancer'
        self.health = physpara.Health(150, 15, level, 'cloned flesh')
        self.shield = physpara.Shield()
        self.armor = physpara.Armor(200, 15, level, 'alloy')
        self.level = level


class Corpus(Enemy):
    def __init__(self):
        pass


# This is only for the programmers benefit
def GetDamageonGrineerLancer():
    impact = float(input('What is the impact damage of the weapon? \n'))
    puncture = float(input('What is the puncture damage of the weapon? \n'))
    slash = float(input('What is the slash damage of the weapon? \n'))
    AM = float(input('What is the armor modifier of the Grinner Lancer? \n'))
    HM = float(input('What is the health modifier of the Grineer Lancer? \n'))
    level = float(input('What is the level of the Grineer Lancer? \n'))

    grineer = GrineerLancer(level)

    return((impact + puncture + slash)
           * ((1 + HM) * (1 + AM)) / (1 + (grineer.armor * (1 - AM)) / 300))
