'''A module containing everything to do with enemies.
'''
import numpy

import _dictionaries


class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.level = level

        if self.name not in _dictionaries.ENEMY_DICT.keys():
            raise Exception('The given enemy name is not in the enemy'
                            'dictionary')

        datagrab = _dictionaries.ENEMY_DICT[self.name]
        self.type = datagrab[0]
        self.min_level = datagrab[1]
        self.health_base = datagrab[2]
        self.health_species = datagrab[3]
        self.armor_base = datagrab[4]
        self.armor_species = datagrab[5]
        self.shield_base = datagrab[6]
        self.shield_species = datagrab[7]
        del datagrab

        self.health = Health(self.health_base, self.min_level,
                             self.level, self.health_species)

        self.armor = Armor(self.armor_base, self.min_level,
                           self.level, self.armor_species)

        self.shield = Shield(self.shield_base, self.min_level,
                             self.level, self.shield_species)

    def restore(self):
        self.health.current_pp = self.health.pp_max_calc()
        self.armor.current_pp = self.armor.pp_max_calc()
        self.shield.current_pp = self.shield.pp_max_calc()


class PhysicalParameter:
    ''' A base class that represents a 'physical parameter' such as
    health or shields.  It should not be instantiated on its'own.
    '''

    type_dict = {None: [0] * 13}

    def __init__(self, basephysicalparameter, baselevel,
                 currentlevel, species):

        self.basephysicalparameter = basephysicalparameter
        self.baselevel = baselevel
        self.currentlevel = currentlevel
        self.species = species
        self.current_pp = self.pp_max_calc()

        # Check to see if species is in type dictionary as it
        # can be an easy mistype
        if self.species not in self.type_dict.keys():
            raise NameError('%s is not a valid type of %s'
                            % (self.species, type(self).__name__))

        self.array = numpy.array(self.type_dict[species])

    def pp_max_calc(self):
        return(self.basephysicalparameter *
               (1 + self.constant1 * (self.currentlevel - self.baselevel)
                ** self.constant2))

    def __iadd__(self, other):
        self.current_pp += other
        return(self)

    def __isub__(self, other):
        self.current_pp -= other
        return(self)

    def __gt__(self, other):
        return(self.current_pp > other)

    def __ge__(self, other):
        return(self.current_pp >= other)

    def __lt__(self, other):
        return(self.current_pp < other)

    def __le__(self, other):
        return (self.current_pp <= other)

    def __add__(self, other):
        return(self.current_pp + other)

    def __sub__(self, other):
        return(self.current_pp - other)

    def __mul__(self, other):
        return(self.current_pp * other)

    def __truediv__(self, other):
        return(self.current_pp / other)


class Health(PhysicalParameter):
    constant1 = 0.015
    constant2 = 2
    type_dict = ({**PhysicalParameter.type_dict, **{ # noqa
        'cloned flesh': [-0.25, 0, 0.25, 0, 0, 0.25, 0, 0,
                         0, -0.5, 0, 0, 0.75],
        'machinery': [0.25, 0, 0, 0, 0.5, 0, -0.25, 0.75, 0,
                      0, 0, 0, -0.25],
        'flesh': [-0.25, 0, 0.25, 0, 0, 0, 0.5, 0, 0, -0.25,
                  0, 0, 0.5],
        'robotic': [0, 0.25, -0.25, 0, 0.5, 0, -0.25, 0, 0,
                    0, 0, 0.25, 0],
        'infested': [0, 0, 0.25, 0, 0, 0.25, 0, 0, 0, 0.75,
                     0, -0.5, -0.5],
        'infested flesh': [0, 0, 0.5, -0.5, 0, 0.5, 0, 0, 0,
                           0.5, 0, 0, 0],
        'fossilized': [0, 0, 0.15, -0.25, 0, 0, -0.5, 0.5,
                       0.75, 0, 0, -0.75, 0],
        'infested sinew': [0, 0.25, 0, 0.25, 0, 0, 0, -0.5,
                           0, 0, 0, 0.5, 0]}})


class Shield(PhysicalParameter):
    ''' The shield class for an enemy.  Blocks damage before the enemies
    health is affected.
    '''

    constant1 = 0.0075
    constant2 = 2
    type_dict = ({**PhysicalParameter.type_dict, **{
        'shield': [0.5, -0.2, 0, 0.5, 0, 0, 0, 0,
                   0, 0, 0.75, -0.25, 0],
        'proto shield': [0.15, -0.5, 0, 0, 0, -0.5, 0.25,
                         0, -0.5, 0, 0.75, 0, 0]}})


class Armor(PhysicalParameter):
    ''' The Armor class for an enemy.  Provides additional resistances
    for an enemies health to resist damage.
    '''

    constant1 = 0.005
    constant2 = 1.75
    type_dict = ({**PhysicalParameter.type_dict, **{
        'ferrite': [0, 0.5, -0.15, 0, 0, 0,
                    0.25, -0.25, 0.75, 0, 0, 0, 0],
        'alloy': [0, 0.15, -0.5, 0.25, -0.5,
                  0, 0, 0, 0, 0, -0.5, 0.75, 0]}})
