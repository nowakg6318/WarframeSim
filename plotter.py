'''A module to containing all of the plotting classes/functions for the
warframe weapon simulator program.
'''

# Imports
import matplotlib.pyplot as plt
import numpy

import simulate


def Plotter(simulation_list: simulate.Simulation,
            x_units='bullet', y_units='damage'):
    ''' Le plot.
    '''

    unit_dict = ({'bullet': [0, 'Bullet Number'], 'time': [1, 'Time'],
                  'ammo': [2, 'Ammo Left'], 'damage': [3, 'Damage'],
                  'total damage': [4, 'Total Damage'],
                  'impact': [5, 'Impact Damage'],
                  'puncture': [6, 'Puncture Damage'],
                  'slash': [7, 'Slash Damage'], 'cold': [8, 'Cold Damage'],
                  'electricity': [9, 'Electrical Damage'],
                  'heat': [10, 'Heat Damage'], 'toxin': [11, 'Toxin Damage'],
                  'blast': [12, 'Blast Damage'],
                  'corrosive': [13, 'Corrosive Damage'],
                  'gas': [14, 'Gas Damage'],
                  'magnetic': [15, 'Magnetic Damage'],
                  'radiation': [16, 'Radiation Damage'],
                  'viral': [17, 'Viral Damage']})

    # Check to make sure x_units and y_units are in unit_dict
    if (x_units not in unit_dict.keys()) or (y_units not in unit_dict.keys()):
        raise Exception('{} or {} is not an available unit'
                        .format(x_units, y_units))

    for simulation in simulation_list:
        # Plot the values
        x_values = ([column[unit_dict[x_units][0]]
                     for column in simulation.array])

        y_values = ([column[unit_dict[y_units][0]]
                     for column in simulation.array])

        plt.scatter(x_values, y_values,
                    c='C' + str(simulation_list.index(simulation)),
                    label=LabelStringCreater(simulation_list, simulation))

        plt.xlabel(unit_dict[x_units][1])
        plt.ylabel(unit_dict[y_units][1])
        plt.title(TitleStringCreator(simulation_list, simulation,
                                     x_units, y_units, unit_dict))
        plt.legend()
    plt.show()


def LabelStringCreater(simulation_list: simulate.Simulation,
                       simulation: simulate.Simulation):
    label_string = ''
    if len(simulation_list) == 1:
        label_string = ('target: Level {} {}, loadout: {}'
                        .format(simulation.target.level,
                                simulation.target.name,
                                simulation.loadout.name))

    if not all([simulation.target.name == simulation_list[0].target.name
                and simulation.target.level == simulation_list[0].target.level
                for simulation in simulation_list]):

        label_string += ('target: Level {} {} '
                         .format(simulation.target.level,
                                 simulation.target.name))

    if not all([simulation.loadout.name == simulation_list[0].loadout.name
                for simulation in simulation_list]):

        label_string += 'loudout: {}'.format(simulation.loadout.name)

    return(label_string)


def TitleStringCreator(simulation_list: simulate.Simulation,
                       simulation: simulate.Simulation,
                       x_units, y_units, unit_dict):

    title_string = ''
    if len(simulation_list) == 1:
        return('{} vs. {}'
               .format(unit_dict[y_units][1],
                       unit_dict[x_units][1]))

    if all([simulation.target.name == simulation_list[0].target.name
            and simulation.target.level == simulation_list[0].target.level
            for simulation in simulation_list]):

        title_string += ('Target: Level {} {}, '
                         .format(simulation.target.level,
                                 simulation.target.name))

    if all([simulation.loadout.name == simulation_list[0].loadout.name
            for simulation in simulation_list]):

        title_string += 'Loudout: {}, '.format(simulation.loadout.name)

    title_string += ('{} vs. {}'
                     .format(unit_dict[y_units][1],
                             unit_dict[x_units][1]))

    return(title_string)
