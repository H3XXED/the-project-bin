# Chapter 11 Testing a function.
# Simple function to generate a name to use for testing.
'''
# This is original code for testing.
def get_formatted_name(first, last):
	"""Generate a neatly formatted full name"""
	full_name = f"{first} {last}"
	return full_name.title()
'''

# Code added to test middle name input
def get_formatted_name(first, middle, last):
	"""Generate a neatly formatted full name"""
	full_name = f"{first} {middle} {last}"
	return full_name.title()



# Code to make middle name optional.
def get_formatted_name(first, last, middle=''):
	"""Generate a neatly formatted full name"""
	if middle:
		full_name = f"{first} {middle} {last}"
	else:
		full_name = f"{first} {last}"
	return full_name.title()
