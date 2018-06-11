''' A module to simulate the damage of a warframe weapon against an
enemy.
'''

# Imports
import numpy
import random
from math import floor

import mods
import enemies
from mod_calculations import calculate_mod_effects


class Simulation():
    ''' Contains all simulated data between a target and a loadout.

    A class that, given a loadout and a target, can simulate all of the
    damage done to that target by that specific loadout.

    Attributes:
        loadout (mods.Loadout): The loadout to damage the target.
        target (enemies.Enemy): The target to be damaged.
        self.array (list -> numpy.array): A 2D array containing all of
            the damage done to the target.  Each column is the damage
            done by a single bullet fired by the weapon.

            This specific variable starts out as a list in order to have
            an unknown length.  It is converted to a numpy array once the
            Simulate function has been run.

    '''

    # Magic Methods
    def __init__(self, loadout: mods.loadout, target: enemies.Enemy):
        self.loadout = loadout
        self.target = target
        self.array = []

    def __str__(self):
        rep_string = ('Weapon: {} '
                      'loadout: {} \n'
                      'Target: Level {} {} \n'
                      .format(self.loadout.weapon_name, self.loadout.name,
                              self.target.level, self.target.name))

        for column in self.array:
            rep_string = (rep_string
                          + 'bullet: {}, time: {:.3f},'
                          'ammo left: {}, damage done: {:.2f} \n'
                          .format(column[0], column[1],
                                  column[2], sum(column[5:])))
        return(rep_string)

    # Properties
    @property
    def shield_damage_array(self):
        ''' numpy.array: A 1D array containing the normal damage done
        to the target's shields by the loadout's weapon.
        '''

        array = numpy.multiply(self.loadout.loadout_array[:13],
                               self.target.shield.array + 1)

        # Get rid of toxin damage, as it doesn't effect shields.
        array[6] = 0
        return(array)

    @property
    def health_damage_array(self):
        ''' numpy.array: A 1D array containing the normal damage done
        to the target's health by the loadout's weapon.
        '''

        health_modifier_array = numpy.array(
            [self._HealthModifierCalc(i) for i in range(13)])
        health_damage_array = numpy.multiply(self.loadout.loadout_array[:13],
                                             health_modifier_array)
        return(health_modifer_array)

    # Private Methods
    def _HealthModifierCalc(self, index: int) -> numpy.float:
        ''' Calculates a health modifier given the damage index.

        Calculates a health modifier, representing the modification to a
        weapon's damage due to the target's armor and health types, given
        an index corresponding to a type of damage.

        Args:
            index: An integer between 0 and 12 representing a type of
                damage. Refer to the mods module for the code.

        Returns:
            A numpy.float representing the damage modification due to the
            target's health and armor types.
        '''

        health_modifier = (((self.target.health.array[index] + 1)
                           * (self.target.armor.array[index] + 1))
                           / (1 + (self.target.armor.current_pp
                              * (1 - self.target.armor.array[index]) / 300)))

        return(health_modifier)

    def _ShootTarget(self):
        ''' Damages the target and stores the data.

            Encompasses the process of shooting the target.  The number
            of bullets fired is first calculated,
        '''
        num_shots_fired = int(self.loadout.loadout_array[20]) + self.Roll(21)
        # An 2D array where the first row is the damage done to the
        # target's health and the second row is the damage done to the
        # target's shields.
        damage_array = numpy.zeros((2, 13))
        for shot in range(num_shots_fired):
            critical_bool = self.Roll(15)
            impact_area = self.IdentifyImpactArea()
            if isinstance(impact_area, enemies.Shield):
                damage_array += self.AttackShields(critical_bool)
            else:
                damage_array += self.AttackHealth(critical_bool)
        damage_array = self.DamageTarget(damage_array)
        self.StoreData(damage_array)

    def _Roll(self, index: int) -> float:
        roll = random.random()
        boolean = 1 if roll < self.loadout.loadout_array[index] else 0
        return(boolean)

    def _IdentifyImpactArea(self):
        if self.target.shield.current_pp:
            return(self.target.shield)
        else:
            return(self.target.health)

    def _EndSimulate(self):
        self.array = numpy.array(self.array)
        self.target.Restore()
        print(self)

    def _AttackShields(self, critical_bool: bool):
        shield_damage = (self.shield_damage_array
                         * self.loadout.loadout_array[16] ** critical_bool)

        toxin_damage = (self.health_damage_array[6]
                        * self.loadout.loadout_array[16]
                        ** critical_bool)

        health_damage = numpy.concatenate((numpy.zeros(5),
                                          numpy.array([toxin_damage]),
                                          numpy.zeros(7)))

        return(numpy.array([health_damage, shield_damage]))

    def _AttackHealth(self, critical_bool: bool):
        health_damage = (self.health_damage_array
                         * self.loadout.loadout_array[16] ** critical_bool)

        return(numpy.array([health_damage, numpy.zeros(13)]))

    def _CalculateEquivalentHealthDamage(self, shield_damage):
        percent_damage_rem = self.target.shield.current_pp / shield_damage
        health_modifer_array = [self.HealthModifierCalc(i) for i in range(13)]
        damage = numpy.divide(shield_damage, 1 + self.target.shield.array)
        health_damage = numpy.multiply(damage * (1 - percent_damage_rem),
                                       health_modifer_array)

        return(health_damage)

    def _DamageTarget(self, damage_array):
        if not self.target.shield < sum(damage_array[1]):
            # This case evaluates if the damage done to the shield
            # is less than the health of the shield, or simply if
            # the health of the target is damaged.
            self.target.shield -= sum(damage_array[1])
            self.target.health -= sum(damage_array[0])
            return(damage_array)
        else:
            # This case evaluates if the damage done to the targets
            # shield is greater than the health of the shield.
            percent_damage_done = self.target.shield / damage_array[1]
            self.target.shield.current_pp = 0
            damage_array[0] += CalculateEquivalentHealthDamage(damage_array[1])
            self.target.health -= sum(damage_array[0])
            damage_array[1] = damage_array[1] * percent_damage_done
            return(damage_array)

    def _StoreData(self, damage_array):
        bullet_count = len(self.array) + 1
        time = (bullet_count
                + floor(bullet_count / self.loadout.loadout_array[18])
                * self.loadout.loadout_array[19])

        ammo = (self.loadout.loadout_array[18]
                - (bullet_count
                    - (floor(bullet_count / self.loadout.loadout_array[18])
                       * self.loadout.loadout_array[18])))

        damage_sum = numpy.sum(damage_array)
        if len(self.array):
            total_damage = damage_sum + sum(self.array[len(self.array) - 1])
        else:
            total_damage = damage_sum
        damage = numpy.add(damage_array[0], damage_array[1])
        self.array.append([bullet_count, time, ammo,
                           damage_sum, total_damage]
                          + list(damage))

    # Public Methods
    def Simulate(self):
        '''Calculates and fills an event list with the damage done to the
        target.
        '''
        calculate_mod_effects(self.loadout, self.target)
        while self.target.health > 0:
            self.ShootTarget()
        self.EndSimulate()
        return(self)


class OrderedList(list):
    def __init__(self, attribute_name: str, *args):
        self.attribute_name = attribute_name
        for arg in args:
            self.add(arg)

    def add(self, new_element):
        attribute_list = ([getattr(element, self.attribute_name)
                           for element in self])

        attribute_list.append(getattr(new_element, self.attribute_name))
        attribute_list = sorted(attribute_list)
        new_element_index = attribute_list.index(
            getattr(new_element, self.attribute_name))

        self.insert(new_element_index, new_element)
