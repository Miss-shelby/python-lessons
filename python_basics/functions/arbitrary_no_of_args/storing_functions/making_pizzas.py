# import pizza

# pizza.make_pizza_with_size(16, 'mushrooms', 'green peppers', 'extra cheese')

# Importing Specific Functions
from pizza import make_pizza_with_size
make_pizza_with_size(4,'mushrooms', 'green peppers')

#  Using as to Give a Function an Alias
#  If the name of a function you’re importing might conflict with an exist
# ing name in your program or if the function name is long, you can use a 
# short, unique alias—an alternate name similar to a nickname for the func
# tion. You’ll give the function this special nickname when you import the 
# function.
#  Here we give the function make_pizza() an alias, mp(), by importing 
# make_pizza as mp. The as keyword renames a function using the alias you 
# provide:

from pizza import make_pizza as mp
mp(16,'pepperoni')

#  The import statement shown here renames the function make_pizza() to 
# mp() in this program. Any time we want to call make_pizza() we can simply 
# write mp() instead, and Python will run the code in make_pizza() while avoid
# ing any confusion with another make_pizza() function you might have writ
# ten in this program file

# NOTE:Using as to Give a Module an Alias
#  You can also provide an alias for a module name. Giving a module a short 
# alias, like p for pizza, allows you to call the module’s functions more quickly. 
# Calling p.make_pizza() is more concise than calling pizza.make_pizza():
import pizza as p
p.make_pizza_with_size(10,'mushrooms')

# NOTE: IMPORTING  ALL FUNCTIONS IN A MODULE
# You can tell Python to import every function in a module by using the aster
# isk (*) operator

from pizza import *
make_pizzas(3,'cheese')