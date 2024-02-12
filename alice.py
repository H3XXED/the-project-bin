# Chapter 10 Handling the FileNotFoundError Exception


from pathlib import Path

path = Path('alice.txt')
'''
contents = path.read_text(encoding='utf-8')
'''

# Adding Try: code to eliminate error.

try:
	contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
	print(f"Sorry, the file {path} does not exist.")
# Adding else block for the file
else:
	# Count the approximate number of words in the file:
	words = contents.split()
	num_words = len(words)
	print(f"The file {path} has about {num_words} words.")

