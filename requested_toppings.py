# Chapter 5 Testing multiple conditions

# requested_toppings = ['mushrooms', 'extra cheese']
'''
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")
'''
'''
# Below is incorrect code would stop running after only one test passes
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")
'''

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
'''
for requested_topping in requested_toppings:
	print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")
'''

'''
# what if pizzaria runs out of peppers
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry we are out of green peppers right now.")
	else:
		print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

'''
'''
# Checking that a list is not empty

requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")
'''
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
