# Chapter 5 The if-else chain

age = int(input("What is your age? "))

'''
if age < 4:
	print("Your admission cost is $0.00!")
elif age < 18:
	print("Your admission cost is $25.00!")
else:
	print("Your admission cost is $40.00!")

'''

'''
if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40

print(f"Your admission cost is ${price}!")
'''
'''
if age < 4:
	price = 0

elif age < 18:
	price = 25

elif age < 65:
	price = 40

else:
	price = 20

print(f"Your admission cost is ${price}!")
'''

# Omitting the else block from above code
if age < 4:
	price = 0

elif age < 18:
	price = 25

elif age < 65:
	price = 40

elif age >= 65:
	price = 20

print(f"Your admission cost is ${price}!")