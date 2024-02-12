from pathlib import Path
import json

'''
username = input("What is your name? ")

path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"We'll remember you when you come back, {username}")
'''
'''
# Combining greet and remember programs to save and read user generated data.
def greet_user():
	path = Path('username.json')
	if path.exists():
		contents = path.read_text()
		username = json.loads(contents)
		print(f"Welcome back, {username}")
	else:
		username = input("What is your name? ")
		contents = json.dumps(username)
		path.write_text(contents)
		print(f"We'll remember you when you come back, {username}")
		
greet_user()
'''


# Rewriting code to use the function to reflect how the program works.

def get_stored_username(path):
	"""Get stored username if available"""
	if path.exists():
		contents = path.read_text()
		username = json.loads(contents)
		return username
	else:
		return None


def get_new_username(path):
	"""Prompt for a new username"""
	username = input("What is your name? ")
	contents = json.dumps(username)
	path.write_text(contents)
	return username


def greet_user():
	"""Greet the user by name."""
	path = Path('username.json')
	username = get_stored_username(path)
	if username:
		print(f"Welcome back, {username}")
	else:
		username = get_new_username(path)
		print(f"We'll remember you when you come back, {username}")


greet_user()
