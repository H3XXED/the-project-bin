# Chapter 3 Modifying elements in a list
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
'''

'''
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
'''

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

# motorcycles.insert(0, 'ducati')
print(motorcycles)

# del motorcycles[0]

# del motorcycles[1]

# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

#last_owned = motorcycles.pop(0)
#print(f"The last motorcycle I owned was a {last_owned.title()}.")


too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")
