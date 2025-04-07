# Sometimes you won’t know ahead of time how many arguments a function 
# needs to accept. Fortunately, Python allows a function to collect an arbi
# trary number of arguments from the calling statement.

# For example, consider a function that builds a pizza. It needs to accept a 
# number of toppings, but you can’t know ahead of time how many toppings 
# a person will want. The function in the following example has one param
# eter, *toppings, but this parameter collects as many arguments as the calling 
# line provides

def make_pizza(*toppings):
      """Print the list of toppings that have been requested."""
      print(toppings)

make_pizza("pepperoni")
make_pizza("mushrooms","green peppers","extra cheese")

def make_pizzas(*toppings):
       """Summarize the pizza we are about to make."""
       print("\nMaking a pizza with the following toppings:")
       for t in toppings:
              print(f" -{t}")
make_pizzas("pepperoni")
make_pizzas("mushrooms","green peppers","extra cheese")


#  NOTE: Mixing Positional and Arbitrary Arguments

#  If you want a function to accept several different kinds of arguments, the 
# parameter that accepts an arbitrary number of arguments must be placed 
# last in the function definition. Python matches positional and keyword 
# arguments first and then collects any remaining arguments in the final 
# parameter.
#  For example, if the function needs to take in a size for the pizza, that 
# parameter must come before the parameter *toppings

def make_pizza_with_size(size,*toppings):
       print(f"\nMaking a {size}-inch pizza with the following toppings:")
       for topping in toppings:
              print(f"-{topping}")

make_pizza_with_size(3,"mushrooms","green peppers","extra cheese")



