# Chapter 10 Working with multiple files

from pathlib import Path


def count_words(path):
	"""Count the approximate number of words in a file."""
	try:
		contents = path.read_text(encoding='utf-8')
	except FileNotFoundError:
		pass # This will cause the error to be ignored and move on to the next part without printing error statement
		# print(f"Sorry, the file {path} does not exist.")
	# Adding else block for the file
	else:
		# Count the approximate number of words in the file:
		words = contents.split()
		num_words = len(words)
		print(f"The file {path} has about {num_words} words.")
		path = Path('alice.txt')



filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
	path = Path(filename)
	count_words(path)
