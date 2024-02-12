# Chapter 10 Is your birthday contained in Pi?

from pathlib import Path

path = Path('pi_million_digits')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
	pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form of mmddyy:")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")