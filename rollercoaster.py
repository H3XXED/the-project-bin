# Chapter 7 Using int() for alphanumerical input.

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you are a little older.")	