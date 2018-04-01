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
    def __init__(self, loadout: mods.loadout, target: enemies.Enemy):
        self.loadout = loadout
        self.target = target
        self.array = []
        self.UpdateShieldDamageArray()
        self.UpdateHealthDamageArray()

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

    def UpdateShieldDamageArray(self):
        array = numpy.multiply(self.loadout.loadout_array[:13],
                               self.target.shield.array + 1)

        # Get rid of toxin damage, as it doesn't effect shields.
        array[6] = 0
        self.shield_damage_array = array

    def UpdateHealthDamageArray(self):
        ### FIX THIS ARRAY ####
        health_modifier_array = [(
            ((self.target.health.array[i] + 1)
             * (self.target.armor.array[i] + 1))
            / (1 + (self.target.armor.current_pp
                    * (1 - self.target.armor.array[i]) / 300)))
            for i in range(13)]

        health_damage_array = numpy.multiply(self.loadout.loadout_array[:13],
                                             health_modifier_array)

        self.health_damage_array = health_damage_array

    def Simulate(self):
        '''Calculates and fills an event list with the damage done to the
        target.
        '''
        calculate_mod_effects(self.loadout, self.target)
        self.UpdateHealthDamageArray()
        self.UpdateShieldDamageArray()
        while self.target.health > 0:
            self.ShootTarget()
        self.EndSimulate()
        return(self)

    def ShootTarget(self):
        num_shots_fired = int(self.loadout.loadout_array[20]) + self.Roll(21)
        for shot in range(num_shots_fired):
            critical_bool = self.Roll(15)
            impact_area = self.IdentifyImpactArea()
            if isinstance(impact_area, enemies.Shield):
                health_array, shield_array = self.AttackShields(critical_bool)
            else:
                health_array, shield_array = self.AttackHealth(critical_bool)
            health_array, shield_array = self.DamageTarget(health_array,
                                                           shield_array,
                                                           critical_bool)
            self.StoreData(health_array, shield_array)

    def Roll(self, index: int) -> float:
        roll = random.random()
        boolean = 1 if roll < self.loadout.loadout_array[index] else 0
        return(boolean)

    def IdentifyImpactArea(self):
        if self.target.shield.current_pp:
            return(self.target.shield)
        else:
            return(self.target.health)

    def EndSimulate(self):
        self.array = numpy.array(self.array)
        self.target.restore()
        print(self)

    def AttackShields(self, critical_bool: bool):
        shield_damage = (self.shield_damage_array
                         * self.loadout.loadout_array[16] ** critical_bool)

        toxin_damage = (self.health_damage_array[6]
                        * self.loadout.loadout_array[16]
                        ** critical_bool)

        health_damage = numpy.concatenate((numpy.zeros(5),
                                          numpy.array([toxin_damage]),
                                          numpy.zeros(7)))

        return(health_damage, shield_damage)

    def AttackHealth(self, critical_bool: bool):
        health_damage = (self.health_damage_array
                         * self.loadout.loadout_array[16] ** critical_bool)

        return(health_damage, numpy.zeros(13))

    def DamageTarget(self, health_damage, shield_damage, critical_bool):
        if not self.target.shield < sum(shield_damage):
            # This case evaluates if the damage done to the shield
            # is less than the health of the shield, or simply if
            # the health of the target is damaged.
            self.target.shield -= sum(shield_damage)
            self.target.health -= sum(health_damage)
            return(health_damage, shield_damage)
        else:
            # This case evaluates if the damage done to the targets
            # shield is greater than the health of the shield.
            percent_damage_done = self.target.shield / sum(shield_damage)
            self.target.shield.current_pp = 0
            health_damage = ((self.health_damage_array
                             * (1 - percent_damage_done)
                             * self.loadout.loadout_array[16]
                             ** critical_bool)
                             + health_damage)

            self.target.health -= sum(health_damage)
            return(health_damage, shield_damage * percent_damage_done)

    def StoreData(self, health_damage, shield_damage):
        bullet_count = len(self.array) + 1
        time = (bullet_count
                + floor(bullet_count / self.loadout.loadout_array[18])
                * self.loadout.loadout_array[19])

        ammo = (self.loadout.loadout_array[18]
                - (bullet_count
                    - (floor(bullet_count / self.loadout.loadout_array[18])
                       * self.loadout.loadout_array[18])))

        damage_sum = sum(health_damage) + sum(shield_damage)
        if len(self.array):
            total_damage = damage_sum + sum(self.array[len(self.array) - 1])
        else:
            total_damage = damage_sum
        damage = numpy.add(health_damage, shield_damage)
        self.array.append([bullet_count, time, ammo,
                           damage_sum, total_damage]
                          + list(damage))
