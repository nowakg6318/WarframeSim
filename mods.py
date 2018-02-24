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
    def __init__(self, name):
        self.name = name

        datagrab = _dictionaries.PRIMARY_MOD_DICT[self.name]

        self.type = datagrab[0]
        self.priority = datagrab[1]
        self.cost = datagrab[2]
        self.polarity = datagrab[3]
        self.if_condition = datagrab[4]
        self.else_condition = datagrab[5]
        self.damage_vector = datagrab[6:18]
        self.accuracy = datagrab[19]
        self.fire_rate = datagrab[20]
        self.critical_chance = datagrab[21]
        self.critical_multipler = datagrab[22]
        self.status_chance = datagrab[23]
        self.magazine_capacity = datagrab[24]
        self.reload_time = datagrab[25]

        self.mod_array = numpy.array(datagrab[6:])
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
        loadout.update_mod_list()
        if mod.name in [mod.name for mod in loadout.mod_list]:
            raise Exception('%s has already been added to this loadout.'
                            '  Please add a different mod.' % mod.name)

        self.mod_name = mod.name
        self.mod = mod

        if self.polarity == mod.polarity:
            mod.cost = math.ceil(mod.cost / 2)

        elif not self.polarity:
            pass

        else:
            mod.cost = math.ceil(mod.cost * 1.25)


class loadout():
    def __init__(self, cursor, name, weapon, polarity_list):
        self.cursor = cursor
        self.name = name
        self.weapon = weapon
        self.points = 60
        self.loadout_array = weapon.weapon_array
        self.loadout_crit_array = numpy.zeros(20)

        self.accuracy = self.loadout_array[13]
        self.fire_rate = self.loadout_array[14]
        self.critical_chance = self.loadout_array[15]
        self.critical_multipler = self.loadout_array[16]
        self.status_chance = self.loadout_array[17]
        self.ammo_capacity = self.loadout_array[18]
        self.reload_time = self.loadout_array[19]

        self.ammo = self.ammo_capacity

        self.modslot_list = [0] * 8
        for index in range(8):
            self.modslot_list[index] = mod_slot(polarity=polarity_list[index])

        self.update_mod_list()

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

    def add_mod(self, *args: mod) -> None:
        '''A function to add mods to the loadout modslots without needing
        to call the modslots individually.  The function will fill the
        first non-empty modslot in sequential order.'''

        self.update_mod_list()
        if len(args) > self.get_number_empty_modslots():
            raise Exception('There are more mods requesting',
                            'to be added then available modslots.')

        list_empty_modslot_index = (
            [self.modslot_list.index(modslot) for modslot
                in self.modslot_list if not modslot.mod])

        for index in range(len(args)):
            self.modslot_list[list_empty_modslot_index[index]].add_mod(
                self, args[index])

        self.calculate_mod_cost()

    def get_number_empty_modslots(self) -> int:
        '''Calculates the number of empty modslots in a loadout.'''

        number_empty_modslots = sum(
            [True for modslot in self.modslot_list if not modslot.mod])

        return number_empty_modslots

    def update_mod_list(self):
        '''A function to update the mod_list with all of the non-empty
        modslots in a loadout. '''

        self.mod_list = [modslot.mod for modslot
                         in self.modslot_list if modslot.mod]

    def calculate_mod_cost(self):
        '''A function to calculate the cost of the current mods in the
        loadout.  This number should not surpass 60.'''

        self.update_mod_list()
        self.points = 60 - sum(mod.cost for mod in self.mod_list)

        if self.points < 0:
            raise Exception('This loadout has too high a cost.',
                            'please change the mods attached to this loadout!',
                            'It is currently unsimulatable.')
        return self.points


if __name__ == '__main__':
    pass
