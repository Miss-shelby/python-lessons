
age = 19

if age>=19:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")

age = 17

if age >= 18:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# elif used when we want to test more than one condidtion
age = 3
if age < 4:
    print('Your admision cost $0 ')
elif age < 18:
     print('Your admision cost $25 ')
else:
     print('Your admision cost $40')


if age < 4:
    price =0
elif age < 18:
     price = 25
else:
     price = 40

print(f"Your admission cost is ${price}")

# multiple if block ,we can omit the else block at the end of n if-elif chain
# If you have a specific final condition you are 
# testing for, consider using a final elif block and omit the else block. 
if age < 4:
    price =0
elif age < 18:
     price = 25
elif age < 65:
     price = 40
elif age >= 65:
     price = 20
print(f"Your admission cost is ${price}")

# testing multiple conditions
# However, sometimes it’s important to check all of the conditions of 
# interest. In this case, you should use a series of simple if statements with no 
# elif or else blocks. This technique makes sense when more than one condition could be True, and you want to act on every condition that is True.
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
     print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
     print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
     print('Adding extra cheese')
print("\n Finished making your pizza!")