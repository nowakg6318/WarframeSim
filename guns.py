# All guns are assumed to be level 30
# There is currently no way to change this
#

# imports
import numpy

import mods


class weapon():
    def __init__(self):
        pass


class gun(weapon):
    def __init__(self, cursor, name):
        self.cursor = cursor
        self.name = name

        # Grab weapon values from database
        datagrab = (cursor.execute(
            '''SELECT * FROM primary_weapons WHERE weapon_name=?''',
            (self.name[0].upper() + self.name[1:].lower(),))
            .fetchall()[0])

        self.mod_type = datagrab[2]
        self.damage_vector = datagrab[3:15]
        self.accuracy = datagrab[16]
        self.fire_rate = datagrab[17]
        self.critical_chance = datagrab[18]
        self.critical_multiplier = datagrab[19]
        self.status_chance = datagrab[20]
        self.magazine_capacity = datagrab[21]
        self.reload_time = datagrab[22]

        self.weapon_array = numpy.array(datagrab[3:23])
        del datagrab

        # Create first loadout
        self.loadout_list = []
        self.add_loadout()

        # Self variables
        self.current_magazine = self.magazine_capacity

    def add_loadout(self):
        polarity_list = (self.cursor.execute(
            '''SELECT mod_polarity_1, mod_polarity_2, mod_polarity_3,
            mod_polarity_4, mod_polarity_5, mod_polarity_6,
            mod_polarity_7, mod_polarity_8 FROM primary_weapons
            WHERE weapon_name=? ''',
            (self.name[0].upper() + self.name[1:].lower(),)).fetchall()[0])

        self.loadout_list.append(mods.loadout(
            self.cursor, "loadout" + str(len(self.loadout_list)),
            self, polarity_list))

        del polarity_list
        return(self.loadout_list[len(self.loadout_list) - 1])
