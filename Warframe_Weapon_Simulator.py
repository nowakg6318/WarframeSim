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
    loadout1 = loadout('Viral', 'Soma')
    loadout1.add_mod(mod('Serration', 10), mod('Infected Clip', 2), mod('Cryo Rounds', 2))
    grineer = enemies.Enemy('Elite Crewman', 25)
    simulation = simulate.Simulation(loadout1, grineer)
    simulation.Simulate()
    plotter.Plotter([simulation])
