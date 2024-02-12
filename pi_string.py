# Chapter 10 Working with a files contents.

from pathlib import Path

path = Path('pi_million_digits')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
	pi_string += line.lstrip()

'''
Hidden to work on million digits
print(pi_string)
print(len(pi_string))
'''

print(f"{pi_string[:52]}...")
print(len(pi_string))