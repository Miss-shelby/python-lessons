# The return statement takes a value 
# from inside a function and sends it back to the line that called the function. 
# Return values allow you to move much of your program’s grunt work into 
# functions, which can simplify the body of your program.

def get_formatted_name(f_name,l_name,m_name=''):
    """Return a fullname, neatly formatted."""
    if m_name:
        full_name = f"{f_name} {l_name} {m_name}" 
    else:
        full_name = f"{f_name} {l_name}" 
    return full_name.title()

musician = get_formatted_name("post","malone")
print(musician)

# NOTE:  When you call a function that returns a value, you need to provide a 
# variable that the return value can be assigned to. In this case, the returned 
# value is assigned to the variable musician

#  Returning a Dictionary

def build_person(f_name,l_name,age=None):
    """return a dictiionary of information bout a person"""
    person ={'first': f_name, 'last':l_name}
    if age:
        person['age'] = age
    return person
musician = build_person("jimi",'hendix',age =25)
print(musician)

# we use none  when a variable 
# has no specific value assigned to it. You can think of None as a placeholder 
# value. In conditional tests, None evaluates to False. 

#  Using a Function with a while Loop

def get_formatted_names(first_name,last_name):
    """return a fullname, neatly formatted."""

    full_names = f"{first_name} {last_name}"
    return full_names.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' anytime to quit)")

    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("last name:")
    if l_name == 'q':
        break
    my_name = get_formatted_names(f_name,l_name)
    print(f"Hello,{my_name}")