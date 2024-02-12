# Chapter 8 Positional arguments

def describe_pet(animal_type, pet_name):
	"""Display information about a pet"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")
'''
describe_pet('hamster', 'harry')
# Makes multiple call outs
describe_pet('dog', 'willie')
'''
# Rewriting with keyword arguments

describe_pet(animal_type='hamster', pet_name='harry')
