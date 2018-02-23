''' A module to simulate the damage of a warframe weapon against an
enemy.
'''

# Imports
import numpy
import random

import mods
import enemies
import mod_calculations as modcalc


class Simulation():
    def __init__(self, loadout: mods.loadout, target: enemies.Enemy):
        self.loadout = loadout
        self.target = target
        self.array = []

    def __str__(self):
        rep_string = ('Weapon: {} '
                      'loadout: {} \n'
                      'Target: Level {} {} \n'
                      .format(self.loadout.weapon.name, self.loadout.name,
                              self.target.level, self.target.name))

        for column in self.array:
            rep_string = (rep_string
                          + 'bullet: {}, time: {:.3f},'
                          'ammo left: {}, damage done: {:.2f} \n'
                          .format(column[0], column[1],
                                  column[2], sum(column[5:])))
        return(rep_string)


def Simulator(*args: Simulation):
    '''Takes several EventLists and runs the simulate function on
    each of them.
    '''

    return([Simulate(arg) for arg in args])


def Simulate(simulation: Simulation):
    '''Calculates and fills an event list with the damage done to the
    target.

    * Look into nonlocal variables.
    '''

    # Definitions
    bullet_count = 0
    time = 0

    # Main Function
    modcalc.calculate_effective_damage_array(simulation.loadout,
                                             simulation.target)
    print(simulation.loadout)
    if simulation.target.shield > 0:
        bullet_count, time = AttackShields(bullet_count, time, simulation)

    AttackHealth(bullet_count, time, simulation)
    simulation.array = numpy.array(simulation.array)
    print(simulation)
    return(simulation)


def AttackShields(bullet_count: int, time: float, simulation: Simulation):
    '''Calculates and fills an event list with the damage done to the
    target, until the targets shields OR health are depleted.


    LOOOK HERE IF THERE ARE ANY MATHEMTICAL MISTAKES WHEN TESTING!
    '''

    # Definitions to  be constant through the execution of shields.
    loadout = simulation.loadout
    target = simulation.target

    while target.health > 0 and target.shield > 0:
        # More Definitions
        toxin_damage_modifer = (
            ((target.health.array[6] + 1) * (target.armor.array[6] + 1))
            / (1 + (target.armor.current_pp
                    * (1 - target.armor.array[6]) / 300)))

        toxin_damage = loadout.loadout_array[6]
        shield_damage_array = numpy.multiply(loadout.loadout_array[:13],
                                             target.shield.array + 1)

        # Get rid of toxin damage
        shield_damage_array[6] = 0

        # Fire a bullet, increase time, and increase bullet number
        bullet_count += 1
        loadout.ammo -= 1
        time = (bullet_count - 1) * (1 / (loadout.fire_rate))

        # Various random effects
        crit_roll = random.random()
        multishot_roll = random.random()
        status_roll = random.random()

        # Damage Modifiers from random effects
        critical_bool = 1 if crit_roll < loadout.critical_chance else 0

        # Deal damage to health and shields
        shield_damage = (sum(shield_damage_array) *
                         loadout.critical_multipler ** critical_bool)

        health_damage = (toxin_damage * toxin_damage_modifer *
                         loadout.critical_multipler ** critical_bool)

        # If the damage done to the shields is less than the health of
        # the shields, then deal the damage and move along.
        if shield_damage <= target.shield:
            target.shield -= shield_damage
            target.health -= health_damage
            damage_array = shield_damage_array
            damage_array[6] = health_damage

        # If the damage done to the shields is greater than the health
        # of the shields, then deal damage to break the shields and deal
        # the rest of the damage to the target's health.
        else:
            percent_damage_done = target.shield / shield_damage
            health_damage_array = numpy.multiply(loadout.loadout_array[:13],
                                                 target.health.array + 1)
            target.shield.current_pp = 0
            target.health -= (sum(health_damage_array)
                              * (1 - percent_damage_done)
                              * loadout.critical_multipler ** critical_bool)

            damage_array = ((percent_damage_done * shield_damage_array
                             + (1 - percent_damage_done) * health_damage_array)
                            * loadout.critical_multipler ** critical_bool)

        # Append the event to the simulation list
        damage_sum = sum(damage_array)
        total_damage = (damage_sum
                        + sum([column[3] for column in simulation.array]))

        simulation.array.append([bullet_count, time, loadout.ammo,
                                 damage_sum, total_damage]
                                + list(damage_array))

        # Reload if needed
        if loadout.ammo == 0:
            time = time + loadout.reload_time
            loadout.ammo = loadout.ammo_capacity

    # Return time and bullet_count
    return bullet_count, time


def AttackHealth(bullet_count: int, time: float, simulation: Simulation):
    '''Calculates and fills an event list with the damage done to the
    target, until the targets health is depleted.


    LOOOK HERE IF THERE ARE ANY MATHEMTICAL MISTAKES WHEN TESTING!
    '''

    # Definitions
    loadout = simulation.loadout
    target = simulation.target

    while target.health > 0:
        # Definitions
        health_modifier_array = [(
            ((target.health.array[i] + 1) * (target.armor.array[i] + 1))
            / (1 + (target.armor.current_pp
                    * (1 - target.armor.array[i]) / 300)))

            for i in range(13)]

        damage_array = numpy.multiply(loadout.loadout_array[:13],
                                      health_modifier_array)

        # Fire a bullet, increase time, and increase bullet number
        bullet_count += 1
        loadout.ammo -= 1
        time = (bullet_count - 1) * (1 / (loadout.fire_rate))

        # Various random effects
        crit_roll = random.random()
        multishot_roll = random.random()
        status_roll = random.random()

        # Damage Modifiers from random effects
        critical_bool = 1 if crit_roll < loadout.critical_chance else 0

        # Deal damage to health
        health_damage_array = (damage_array *
                               loadout.critical_multipler ** critical_bool)

        target.health -= sum(health_damage_array)

        # Store the data for this shot in the simulation array
        damage_sum = sum(health_damage_array)
        total_damage = (damage_sum
                        + sum([column[3] for column in simulation.array]))

        simulation.array.append([bullet_count, time, loadout.ammo,
                                 damage_sum, total_damage]
                                + list(health_damage_array))

        # Reload if needed
        if loadout.ammo == 0 and target.health > 0:
            time += loadout.reload_time
            loadout.ammo = loadout.ammo_capacity

    # Return time and bullet_count
    return bullet_count, time
