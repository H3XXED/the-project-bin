# Chapter 7 Introducing while loops
'''
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1
'''

# Using continue in a loop
'''
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue

	print(current_number)
'''

# Avoiding infinite loops

x = 1
while x <= 5:
	print(x)
	x += 1 # If this line is not here it creates the infinite loop.

