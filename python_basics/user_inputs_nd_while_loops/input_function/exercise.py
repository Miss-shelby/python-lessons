car = input("what kind of rental car would you like?")

print(f"\nLet me see if i can find you a {car}")

dinner_group = input("How many people are in your dining group")
dinner_group = int(dinner_group)

if dinner_group >= 8:
    print("You will have to wait for a table")
else:
    print('Your table is ready ')

number = input('Enter a number and i will tell you if its a multiple of 10')

number = int(number)

if 10 % number  ==0:
    print(f"\nThe number {number} is a multiple of 10")
else:
    print(f"\nThe number {number} is not a multiple of 10")