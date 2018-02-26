# All guns are assumed to be level 30
# There is currently no way to change this
#

# imports
import numpy

import mods
import _dictionaries


class weapon():
    def __init__(self):
        pass


class gun(weapon):
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
        del datagrab

        # Create first loadout
        self.loadout_list = []
        self.add_loadout()

        # Self variables
        self.current_magazine = self.magazine_capacity

    def add_loadout(self):
        polarity_list = _dictionaries.PRIMARY_DICT[self.name][22:]

        self.loadout_list.append(mods.loadout('loadout'
                                              + str(len(self.loadout_list)),
                                              self, polarity_list))

        del polarity_list
        return(self.loadout_list[len(self.loadout_list) - 1])
