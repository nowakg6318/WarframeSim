'''
A program to simulate the damage done by weapons in the videogame
warframe.
'''

# Imports
import sqlite3

from guns import gun
from mods import mod
import enemies
import mod_calculations as modcalc
import simulate
import plotter


# Convenience functions
def Start(cursor):
    '''A function to start the weapon simulation process
    by collecting the name of the weapon the user would
    like to simulate.  The name is checked against the
    primary weapons database to ensure it exists.

    Things to do:
        * Eventually this function should check to make sure only ONE names
        comes up from the data base and not 2+.'''

    i = 0
    print('What weapon would you like to simulate? \n')
    weapon_name = str('Soma')

    # Test if gun name exists in database
    while i < 1:
        if (cursor.execute
                ('''SELECT weapon_name FROM primary_weapons
                 WHERE weapon_name=?''',
                 (weapon_name[0].upper() + weapon_name[1:].lower(),))
                .fetchall()):
            return weapon_name

        else:
            print('%s was not found in the primary weapons database,',
                  'please enter a valid weapon name.' % weapon_name)
            weapon_name = input('')


# Main Function
if __name__ == "__main__":
    # Play around
    Soma = gun('Soma')
    loadout1 = Soma.loadout_list[0]
    loadout1.add_mod(mod('Serration', 10))
    loadout1.modslot_list[1].add_mod(loadout1, mod('Hellfire', 1))
    grineer = enemies.EliteLancer(15)
    simulation_list = simulate.Simulator(simulate.Simulation(loadout1, grineer))
    plotter.Plotter(simulation_list, y_units='damage')
