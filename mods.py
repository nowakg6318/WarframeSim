'''A module containing classes relating to mods used in the warframe
weapon simulator.
'''

'''There are three categories of mods in this program: functional,
partially functional, and non-functional.  Functional mods are totally
implemented into the program.  Partially functional mods have some of
their enhancements implemented into the program, but other enhancements
from the mod are not included due to assumptions in the weapon
simulator.  For example, Heavy Caliber increases base damage, but
reduces weapon accuracy.  Since all shots are assumed to hit the target
the accuracy portion of the weapon is calculated, but not implemented.
Lastly, Non-Functional mods are not implemented at all: Argon Scope.'''

'''Arrays take the form:
Impact, Puncture, Slash, Cold, Electricity, Heat, Toxin, Blast,
Corrosive, Gas, Magnetic, Radiation, Viral, accuracy, fire_rate,
critical_chance, critical_multipler, status_chance, ammo_capacity,
reload_time '''

#  Imports
import numpy # noqa E402
from typing import Any # noqa E402

import _dictionaries # noqa E402
import enemies # noqa E402


class mod(object):
    def __init__(self, name, level, datagrab=[None]):
        self.name = name
        self.level = level

        if not any(datagrab):
            datagrab = _dictionaries.PRIMARY_MOD_DICT[self.name]

        self.type = datagrab[0]
        self.priority = datagrab[1]
        self.base_cost = datagrab[2]
        self.max_level = datagrab[3]
        self.polarity = datagrab[4]
        self.if_condition = datagrab[5]
        self.damage_vector = datagrab[6:18]
        self.accuracy = datagrab[19]
        self.fire_rate = datagrab[20]
        self.critical_chance = datagrab[21]
        self.critical_multipler = datagrab[22]
        self.status_chance = datagrab[23]
        self.magazine_capacity = datagrab[24]
        self.reload_time = datagrab[25]

        # Check to see if given level is higher than max level
        if self.level > self.max_level:
            raise Exception('The given level, {}, is greater than the'
                            ' maximum allowable level, {}, for this mod.'
                            .format(self.level, self.max_level))

        self.mod_array = numpy.array(datagrab[6:]) * (self.level + 1)
        self.cost = self.base_cost + self.level
        del datagrab

    def get_modarray(self, characteristic: Any = None) -> numpy.array:  # noqa W291
        '''A function to determine if a mod's enhancements should be
        applied.

        Evaluates the characteristic against the if_condition of the
        mod.  If the condition is true the mod_array is returned, else
        an array of 1's is returned '''
        if eval(self.if_condition):
            return self.mod_array
        else:
            return [1] * len(self.mod_array)


class ProxyMod(mod):
    def __init__(self, elemental_damage_array):
        mod.__init__(self, 'Proxy Mod', 0,
                     numpy.array(2 * [None] + [0, 0] + [None] + ['True']
                                 + [0] * 3 + list(elemental_damage_array)
                                 + [0] * 13))


class mod_slot():
    def __init__(self, polarity=None, mod=None):
        self.polarity = polarity
        self.mod = mod
        self.mod_name = None

    def __str__(self):
        return('mod_slot: \n polarity = {} \n mod = {}\n'.format(
            self.polarity, self.mod_name))

    def add_mod(self, loadout, mod):
        '''A function to add a mod into a modslot, and recalculates the
        cost of the mod. '''

        import math

        # Check to see if the thing being added is a mod
        # Not sure what is wrong here, but fix this.
        if mod.__class__.__name__ != 'mod':
            raise Exception(
                '%s is not a mod and cannot be fit into this mod slot'
                % mod)

        # Check to see if a mod of the same name has already been added
        if mod.name in [mod.name for mod in loadout.mod_list]:
            raise Exception('%s has already been added to this loadout.'
                            '  Please add a different mod.' % mod.name)

        # Check to see if the mod is compatible with the weapon
        if not mod.type == loadout.weapon_mod_type:
            # Check to see if the weapon is a bow
            if (mod.type == 'Rifle' and loadout.weapon_mod_type == 'Bow'):
                pass
            else:
                raise Exception('{} is not compatible with the {} weapon type'
                                .format(mod.name, loadout.weapon_mod_type))

        self.mod_name = mod.name
        self.mod = mod

        if self.polarity == mod.polarity:
            mod.cost = math.ceil(mod.cost / 2)

        elif not self.polarity:
            pass

        else:
            mod.cost = math.ceil(mod.cost * 1.25)


class gun():
    def __init__(self, name):
        self.name = name[0].upper() + name[1:].lower()

        # Grab weapon values from database
        datagrab = _dictionaries.PRIMARY_DICT[self.name]

        self.mod_type = datagrab[1]
        self.damage_vector = datagrab[2:14]
        self.accuracy = datagrab[15]
        self.fire_rate = datagrab[16]
        self.critical_chance = datagrab[17]
        self.critical_multiplier = datagrab[18]
        self.status_chance = datagrab[19]
        self.magazine_capacity = datagrab[20]
        self.reload_time = datagrab[21]

        self.weapon_array = numpy.array(datagrab[2:22])
        self.polarity_list = datagrab[22:]
        del datagrab

        # Self variables
        self.current_magazine = self.magazine_capacity


class loadout():
    def __init__(self, name, weapon_name):
        self.name = name
        self.weapon = gun(weapon_name)

        self.points = 60
        self.weapon_mod_type = self.weapon.mod_type
        self.loadout_array = self.weapon.weapon_array
        self.accuracy = self.loadout_array[13]
        self.fire_rate = self.loadout_array[14]
        self.critical_chance = self.loadout_array[15]
        self.critical_multipler = self.loadout_array[16]
        self.status_chance = self.loadout_array[17]
        self.ammo_capacity = self.loadout_array[18]
        self.reload_time = self.loadout_array[19]
        self.ammo = self.ammo_capacity

        self.modslot_list = [0] * 8
        polarity_list = self.weapon.polarity_list
        for index in range(8):
            self.modslot_list[index] = mod_slot(polarity=polarity_list[index])

    def __str__(self):
        return(
            'Loadout: \n'
            ' Weapon: {} '
            ' Loadout Number: {} \n \n'
            ' Polarity Slots: {} \n'
            ' Mods: {} \n'
            ' Points Left: {} \n \n'
            ' Damage: \n'
            ' Impact: {:.2f}, Puncture: {:.2f}, Slash: {:.2f} \n'
            ' Cold: {:.2f}, Electricity: {:.2f}, Heat: {:.2f},'
            ' Toxin: {:.2f} \n Blast: {:.2f}, Corrosive: {:.2f},'
            ' Gas: {:.2f}, Magnetic: {:.2f}, Radiation: {:.2f},'
            ' Viral: {:.2f} \n \n'
            ' Stats: \n'
            ' Accuracy: {}, Fire Rate: {}, Critical Chance: {},'
            ' Critical Multiplier: {} \n Status Chance: {},'
            '  Ammo Capacity: {}, Reload Time: {} \n'
            .format(self.weapon.name, self.name,
                    [modslot.polarity for modslot in self.modslot_list],
                    [mod.name for mod in self.mod_list],
                    self.calculate_mod_cost(),
                    self.loadout_array[0], self.loadout_array[1],
                    self.loadout_array[2], self.loadout_array[3],
                    self.loadout_array[4], self.loadout_array[5],
                    self.loadout_array[6], self.loadout_array[7],
                    self.loadout_array[8], self.loadout_array[9],
                    self.loadout_array[10], self.loadout_array[11],
                    self.loadout_array[12], self.loadout_array[13],
                    self.loadout_array[14], self.loadout_array[15],
                    self.loadout_array[16], self.loadout_array[17],
                    self.loadout_array[18], self.loadout_array[19])


        )

    @property
    def mod_list(self):
        '''A function to update the mod_list with all of the non-empty
        modslots in a loadout. '''

        return([modslot.mod for modslot
                in self.modslot_list if modslot.mod])

    def add_mod(self, *args: mod) -> None:
        '''A function to add mods to the loadout modslots without needing
        to call the modslots individually.  The function will fill the
        first non-empty modslot in sequential order.'''

        number_empty_modslots = sum(
            [True for modslot in self.modslot_list if not modslot.mod])

        if len(args) > number_empty_modslots:
            raise Exception('There are more mods requesting',
                            'to be added then available modslots.')

        list_empty_modslot_index = (
            [self.modslot_list.index(modslot) for modslot
                in self.modslot_list if not modslot.mod])

        for index in range(len(args)):
            self.modslot_list[list_empty_modslot_index[index]].add_mod(
                self, args[index])

        self.calculate_mod_cost()

    def calculate_mod_cost(self):
        '''A function to calculate the cost of the current mods in the
        loadout.  This number should not surpass 60.'''

        self.points = 60 - sum(mod.cost for mod in self.mod_list)

        if self.points < 0:
            raise Exception('This loadout has too high a cost.',
                            'please change the mods attached to this loadout!',
                            'It is currently unsimulatable.')
        return self.points


if __name__ == '__main__':
    pass
