'''
A program to simulate the damage done by weapons in the videogame
warframe.

Things to do:
  * Give an option for the user to print out all of the valid weapon names.
'''

# Imports
import sqlite3

from guns import gun
from mods import mod
import enemies
import mod_calculations as modcalc
import simulate


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

    # Establish connection to database
    connection = sqlite3.connect('Warframe.db')
    cursor = connection.cursor()

    # Play around
    Soma = gun(cursor, 'Soma')
    loadout1 = Soma.loadout_list[0]
    loadout1.add_mod(mod('Serration'))
    grineer = enemies.GrineerLancer(15)
    eventlist = simulate.Simulate(simulate.EventList(loadout1, grineer))
    for event in eventlist:
        print(event.damage_total, event.damage_array)
