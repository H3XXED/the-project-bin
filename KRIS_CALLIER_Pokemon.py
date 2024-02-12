import json

'''
Function to count the total count of Pokemon 
    Parameters:
        data (list): A list of dictionaries, where each dictionary contains information about a Pokemon.
    Returns:
        int: Total count of Pokemon.
    '''


def get_total_count(data):
    total_count = len(data)
    return total_count


'''
Function takes a list of Pokemon data and returns a dictionary with types of Pokemon and their counts.
    Parameters:
        data (list): A list of dictionaries, where each dictionary contains information about a Pokemon.
    Returns:
        dict: A dictionary with Pokemon types and associated counts.
'''


def get_type_counts(data):
    type_counts = {}
    for pokemon in data:
        for p_type in pokemon['type']:
            if p_type in type_counts:
                type_counts[p_type] += 1
            else:
                type_counts[p_type] = 1
    return type_counts


'''
Function takes a list of Pokemon data and returns the number of Pokemon who have a weight greater than 50 kg.
    Parameters:
        data (list): A list of dictionaries, where each dictionary contains information about a Pokemon.
    Returns:
        int: The number of Pokemon with weight greater than 50 kg.
'''


def get_weight_count(data):
    weight_count = 0
    for pokemon in data:
        weight = pokemon['weight']
        if float(weight.split()[0]) > 50:
            weight_count += 1
    return weight_count


'''
Function takes a list of Pokemon data and returns the .
    Parameters:
        data (list): A list of dictionaries, where each dictionary contains information about a Pokemon.
    Returns:
        int: The count and name of most common weakness
'''


def get_most_common_weakness(data):
    weakness_counts = {}
    for pokemon in data:
        for weakness in pokemon['weaknesses']:
            if weakness in weakness_counts:
                weakness_counts[weakness] += 1
            else:
                weakness_counts[weakness] = 1
    most_common_weakness = max(weakness_counts, key=weakness_counts.get)
    return most_common_weakness


if __name__ == '__main__':
    with open('pokemon.json', 'r') as f:
        data = json.load(f)['pokemon']

    print("Total count of Pokemon:", get_total_count(data))
    print("Types of Pokemon and associated counts:")
    for p_type, count in get_type_counts(data).items():
        print(p_type + ":", count)
    print("Number of Pokemon with weight greater than 50 kg:", get_weight_count(data))
    print("Most common weakness:", get_most_common_weakness(data))
