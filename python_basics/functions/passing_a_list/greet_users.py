#  You’ll often find it useful to pass a list to a function, whether it’s a list of 
# names, numbers, or more complex objects, such as dictionaries. When you 
# pass a list to a function, the function gets direct access to the contents of 
# the list. Let’s use functions to make working with lists more efficient.

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg =f"Hello, {name.title()}!"
        print(msg)
usernames=['hannah','ty','margot']
greet_users(usernames)

# Modifying a List in a Function
# unprinted_designs =['phone case', 'robot pendant', 'dodecahedron']
# completed_models =[]

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)
# print("\nThe following models have been printed:")
# for completed in completed_models:
#     print(completed)

# replicating with function 


def print_models(unprinted_designs, completed_models):
     """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """ 
     while unprinted_designs:
        current_design = unprinted_designs.pop()
        completed_models.append(current_design)
        print(f"Printing models:{current_design}")

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been completed")
    for c in completed_models:
        print(c)


unprinted_designs =['phone case', 'robot pendant', 'dodecahedron']
completed_models =[]

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#  Preventing a Function from Modifying a List
#  Sometimes you’ll want to prevent a function from modifying a list. For 
# example, say that you start with a list of unprinted designs and write a 
# function to move them to a list of completed models, as in the previous 
# example. You may decide that even though you’ve printed all the designs, 
# you want to keep the original list of unprinted designs for your records. 
# 145
#  Functions   
# But because you moved all the design names out of unprinted_designs, the 
# list is now empty, and the empty list is the only version you have; the origi
# nal is gone. In this case, you can address this issue by passing the function a 
# copy of the list, not the original. Any changes the function makes to the list 
# will affect only the copy, leaving the original list intact.
#  You can send a copy of a list to a function like this

print_models(unprinted_designs[:],completed_models)