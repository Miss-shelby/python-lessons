# we use def to define a function in python 

# The text at line 2  is a comment called a docstring, which describes 
# what the function does. Docstrings are enclosed in triple quotes, which 
# Python looks for when it generates documentation for the functions in your 
# programs.
def greet_user(username):
    """ Display a simple greeting"""
    print(f'Hello,{username.title()}!')
greet_user('jesse')

# try it yourself
def display_message():
    print("I am learning about python functions in this chapter")
display_message()

def favourite_book(title):
    print(f"one of my favourite book is: {title.title()}")

favourite_book("The subtle art of not giving a fuck")

# positional arguments
def describe_pets(animal_type,pet_name):
    """Display inormation about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pets("hamster", "harry")
describe_pets("dog",'willie')
# Keyword Arguments
describe_pets(animal_type='cat',pet_name='olive')

#  Default Values
def describe_pets(pet_name,animal_type ='dog'):
     print(f"\nI have a {animal_type}")
     print(f"\nMy {animal_type}'s name is {pet_name.title()}.")
describe_pets(pet_name='jimmy')
# overriding default value 
describe_pets(pet_name='parrot',animal_type='bird')

# try it yourself
def make_shirt(s='large',message='i love python'):
    print(f"My shirt size is {s.title()} and {message} ")
# make_shirt('small')
# make_shirt(s='small')

make_shirt()
make_shirt("medium")
make_shirt("small")
make_shirt('extra large','i love c#')

def describe_city(name,country='US'):
    print(f"{name.title()} is in {country.title()}")
describe_city('newyork')
describe_city('mexico')
describe_city('manchester','UK')