'''
A program to simulate the damage done by weapons in the videogame
warframe.
'''

# Imports

from mods import mod, loadout
import enemies
import simulate
import plotter


# Main Function
if __name__ == "__main__":
    # Play around
    loadout1 = loadout('loadout1', 'Synapse')
    loadout1.add_mod(mod('Infected Clip', 4))
    loadout2 = loadout('loadout2', 'Synapse')
    loadout2.add_mod(mod('Infected Clip', 4), mod('Serration', 5))
    grineer = enemies.Enemy('Grineer Lancer', 15)
    simulation_list = simulate.Simulator(simulate.Simulation(loadout1, grineer),
                                         simulate.Simulation(loadout2, grineer))
    #plotter.Plotter(simulation_list, y_units='damage')
