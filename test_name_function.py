# Chapter 11 A passing test

from name_function import get_formatted_name

# This is a passing test.
def test_first_last_name():
	"""Do names like 'Janis Joplin' work?"""
	formatted_name = get_formatted_name('janis', 'joplin')
	assert formatted_name == 'Janis Joplin'

# Adding New Tests

def test_first_last_middle_name():
	"""Do names like 'Wolfgang Amadeus Mozart' work"""
	formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
	assert formatted_name == 'Wolfgang Amadeus Mozart'


