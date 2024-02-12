# Chapter 10 Reading from a file.

from pathlib import Path

path = Path('pi_digits')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
	print(line)