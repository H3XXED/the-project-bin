# Chapter 8 Importing an Entire Module
'''
import pizza_module

pizza_module.make_pizza(16, 'pepperoni')
pizza_module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''

'''
# Importing Specific Functions
from pizza_module import make_pizza

make_pizza(32, 'pepperoni', 'sausage', 'onion')
make_pizza(28, 'extra cheese', 'black olives', 'ham')
'''
'''
# Using as to Give a Function an Alias
from pizza_module import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese', 'black olives')
'''
'''
# Using as to Give a Module an Alias
import pizza_module as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''

# importing all Functions in a module

from pizza_module import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'onions', 'extra cheese')