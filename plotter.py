'''A module to containing all of the plotting classes/functions for the
warframe weapon simulator program.
'''

# Imports
import matplotlib.pyplot as plt
import numpy

import simulate


def Plotter(eventlist_list: simulate.EventList):
    number_simulations = len(eventlist_list)
    for i in range(len(eventlist_list)):
        eventlist = eventlist_list[i]
        label_string = ('target: Level {} {}, loadout: {}'
                        .format(eventlist.target.level, eventlist.target.name,
                                eventlist.loadout.name))
        x_values = [event.time for event in eventlist]
        y_values = [event.damage_total for event in eventlist]
        plt.scatter(x_values, y_values, c='C' + str(i), label=label_string)
        plt.xlabel('Time (s)')
        plt.ylabel('Damage per Bullet')
        plt.legend()
    plt.show()
