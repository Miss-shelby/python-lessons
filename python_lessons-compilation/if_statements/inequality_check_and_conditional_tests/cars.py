cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car ='bmw'
print(car == 'bmw') #true 
car ='Audi'
print(car == 'audi') #false case sensitive '
print(car.lower() == 'audi') 

# inequality 
requested_topping ='mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# checking multiple conditions 
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)


age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# using or statement
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21) 

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

# we can check if a value its contained in a list viz:
requested_toppings =['ketchup','pepperoni','onions','pineapple']

print ('mushroom' in requested_toppings,'checking if the  value exist is a list')

# checking whether a value is not a list 

banned_users =['andrew','carolina','david']

user ='marie'
if user not in banned_users:
    print(f"{user.title()},you aren't banned so post a response if you wish ")
