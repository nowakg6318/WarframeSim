'''A module to simulate the weapon damage of a weapon in warframe
 against a specific target using a specific loadout.

 Things to do:
'''

# Imports
import numpy
from typing import Any

import mods
import enemies


def calculate_effective_damage_array(loadout: mods.loadout,
     target: enemies.Enemy, characteristic: Any=None) -> numpy.array: # noqa
    ''' A function to combine each of the individual steps in
    calculating the effective damage array of a warframe
    weapon loadout.  The function calls each step systematically.
    The steps are as given below:

    0 - Non-Damage
    1 - Base Damage
    2 - First Elemental Damage
    3 - Second Elemental Damage
    4 - Physical Damage
    5 - Multishot *** Currently Ignored ***
    6 - Critical Damage
    7 - Faction Damages
    8 - Punchthrough *** Currently Ignored '''

    non_damage_mod_calc(loadout)
    base_damage_mod_calc(loadout)
    first_elemental_mod_calc(loadout)
    second_elemental_mod_calc(loadout)
    physical_damage_mod_calc(loadout)
    critical_damage_mod_calc(loadout)
    faction_damage_mod_calc(loadout, target)


def get_relevant_mod_list(loadout: mods.loadout, priority: int) -> list:
    ''' A function to create a list of mods meeting a certain priority
    from a loadout.'''

    loadout.update_mod_list()  # Get rid of this.
    relevant_mod_list = [mod for mod in loadout.mod_list
                         if priority in mod.priority]

    return relevant_mod_list


def non_damage_mod_calc(loadout: mods.loadout) -> None:
    ''' Calculates the enhancements of non-damage type mods such as
    fire rate, accuracy, critical chance, ... , etc. '''
    import copy

    relevant_mod_list = get_relevant_mod_list(loadout, 0)
    loadout_array = copy.deepcopy(loadout.weapon.weapon_array)
    mod_array = numpy.zeros(20)
    for mod in relevant_mod_list:
        mod_array = numpy.add(mod_array, mod.get_modarray() - 1)
    loadout_array[13:] = numpy.multiply(
        loadout_array[13:], mod_array[13:])

    loadout.loadout_array = loadout_array


def base_damage_mod_calc(loadout: mods.loadout) -> None:
    ''' Calculates the enhancements of base damage mods that
    equally effects puncture, impact, and slash damages. '''

    relevant_mod_list = get_relevant_mod_list(loadout, 1)
    loadout_array = loadout.loadout_array
    mod_array = numpy.zeros(20)
    for mod in relevant_mod_list:
        mod_array = numpy.add(mod_array, mod.get_modarray() - 1)
    loadout_array[:3] = (numpy.multiply(
        loadout_array[:3], mod_array[:3]))

    loadout.loadout_array = loadout_array


def first_elemental_mod_calc(loadout: mods.loadout) -> None:
    ''' Calculates the enhancements of first level elemental damage
    mods. '''

    relevant_mod_list = get_relevant_mod_list(loadout, 2)
    loadout_array = loadout.loadout_array
    for mod in relevant_mod_list:
        mod_array = mod.get_modarray()
        sum_of_physical_damage = (loadout_array[0]
                                  + loadout_array[1]
                                  + loadout_array[2])

        non_zero_element = numpy.nonzero(mod_array[:13] - 1)[0]
        loadout_array[non_zero_element] = (
            mod_array[non_zero_element] * sum_of_physical_damage
            + loadout_array[non_zero_element])

    loadout.loadout_array = loadout_array


def second_elemental_mod_calc(loadout: mods.loadout) -> None:
    ''' Calculates the enhancements of the combination of first level
    elemental damage.

    Things to do:
        * Check for twice listed elements in first element array and
         delete any copies.  Then we wont have two cases of the same
        element in each loadout.'''

    # Imports
    import math

    # Definitions
    elemental_dict = ({(0, 1): 10, (1, 0): 10, (0, 2): 7, (2, 0): 7,
                       (0, 3): 12, (3, 0): 12, (1, 2): 11, (2, 1): 11,
                       (1, 3): 8, (3, 1): 8, (3, 2): 9, (2, 3): 9})

    loadout_array = loadout.loadout_array
    relevant_mod_list = get_relevant_mod_list(loadout, 2)

    # Ensure there are no duplicates of the same element
    # in the relevant mod list
    mod_element_index_list = []
    for mod in relevant_mod_list:
        mod_array = mod.mod_array
        mod_element_index = numpy.nonzero(mod_array[3:7] - 1)[0]
        if mod_element_index not in mod_element_index_list:
            mod_element_index_list.append(mod_element_index)
        else:
            del relevant_mod_list[relevant_mod_list.index(mod)]

    # Match first elemental pairs to second elemental type and
    # calculate final second elemental damage
    number_even_pairs_elements = math.floor(len(relevant_mod_list) / 2)
    for index in range(number_even_pairs_elements):
        first_mod_array = relevant_mod_list[2 * index].get_modarray()
        first_mod_element_index = numpy.nonzero(first_mod_array[3:7] - 1)[0]

        second_mod_array = relevant_mod_list[2 * index + 1].get_modarray()
        second_mod_element_index = numpy.nonzero(second_mod_array[3:7] - 1)[0]

        key = (first_mod_element_index[0], second_mod_element_index[0])
        if key not in elemental_dict.keys():
            continue  # Is this the right command?
        loadout_array[elemental_dict[key]] = (
            loadout_array[first_mod_element_index + 3]
            + loadout_array[second_mod_element_index + 3])

        loadout_array[first_mod_element_index + 3] = 0
        loadout_array[second_mod_element_index + 3] = 0


def physical_damage_mod_calc(loadout: mods.loadout) -> None:
    ''' Calculates the enhancements of physical damage bonus
     mods. '''

    relevant_mod_list = get_relevant_mod_list(loadout, 4)
    loadout_array = loadout.loadout_array
    for mod in relevant_mod_list:
        mod_array = mod.get_modarray()
        loadout_array[:3] = numpy.multiply(
            loadout_array[:3], mod_array[:3])

    loadout.loadout_array = loadout_array


def multishot_damage_mod_calc(loadout: mods.loadout) -> None:
    pass


def critical_damage_mod_calc(loadout: mods.loadout) -> None:
    '''Calculates the critical damage and effective critical chance
    of the loadout.'''

    # Imports
    import math

    import copy
    real_critical_chance = (loadout.loadout_array[15]
                            - math.floor(loadout.loadout_array[15]))

    loadout.loadout_array[15] = real_critical_chance
    loadout.loadout_crit_array = copy.deepcopy(loadout.loadout_array)
    loadout.loadout_array[:13] = (loadout.loadout_array[:13]
                                  * loadout.loadout_array[16]
                                  ** math.floor(real_critical_chance))

    loadout.loadout_crit_array[:13] = (loadout.loadout_array[:13]
                                       * loadout.loadout_array[16]
                                       ** math.ceil(
                                       real_critical_chance))


def faction_damage_mod_calc(loadout: mods.loadout,
                            target: enemies.Enemy) -> None:  # noqa
    '''Calculates the enhancements of faction damage mods. '''

    relevant_mod_list = get_relevant_mod_list(loadout, 7)
    loadout_array = loadout.loadout_array
    loadout_crit_array = loadout.loadout_crit_array
    for mod in relevant_mod_list:
        mod_array = mod.get_modarray(characteristic=target)
        loadout_array[:13] = numpy.multiply(
            loadout_array[:13], mod_array[:13])

        loadout_crit_array[:13] = numpy.multiply(
            loadout_crit_array[:13], mod_array[:13])

    loadout.loadout_array = loadout_array
    loadout.loadout_crit_array = loadout_crit_array
