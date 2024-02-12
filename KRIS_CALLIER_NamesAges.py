import re

# Define the string
string_one = '''Jane is 30, her mom Beth is 58 and her dad Jim is 61; while her siblings Joe and Mark are 28 and 32 respectively'''

# Use regular expressions to extract the names and ages
name_age_pairs = re.findall(r'([A-Z][a-z]+)\s+(?:is\s+)?(\d+)', string_one)

# Create a dictionary with names as keys and ages as values
names_ages_dict = {}
for pair in name_age_pairs:
    name = pair[0]
    age = int(pair[1])
    names_ages_dict[name] = age

# Display the dictionary
print(names_ages_dict)

