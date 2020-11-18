"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils

UNARMED_POWER = 20

class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""



	@classmethod
	def make_unarmed(cls):
		unarmed = Weapon("Unarmed", UNARMED_POWER, 1)
		return unarmed

	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self):
		return self.__name


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, name, max_hp, attack, defense, level, weapon=None, hp=None):
		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = weapon
		self.hp = max_hp

	def compute_damage(self, attacker, defender):
		crit_choice = [1, 2]
		crit = random.choices(crit_choice, weights=[15 / 16, 1 / 16])[0]
		random_value = random.uniform(0.85, 1)
		modifier = crit * random_value

		damage = ((((((2 * attacker.level) / 5) + 2) * (attacker.weapon.power) * (attacker.attack / defender.defense)) / 50) + 2) * modifier

		return damage


def deal_damage(attacker, defender): #change hp and show it
	# TODO: Calculer dégâts
	damage_took = attacker.compute_damage(attacker, defender)
	defender.hp -= damage_took

	return print(f"{attacker.name} used {attacker.weapon.name}\n"
				f"{defender.name} took {damage_took} dmg, he has {defender.hp}hp left")


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	print(f"{c1.name} starts a battle with {c2.name}!")
	round = 1
	while c1.hp > 0:
		deal_damage(c1, c2)
		c1, c2 = c2, c1
		round += 1
	return round

