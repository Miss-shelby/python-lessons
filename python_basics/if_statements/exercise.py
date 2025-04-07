car ='subaru'
print("Is car == 'subaru'? I predict TRUE")

print(car == 'subaru')

print("\nIs car == 'audi'?I predict false")
print(car == 'audi')

alien_color ='green'

# if alien_color == 'green':
#     print("Player just earned 5 points ")

# if alien_color == 'red':
#     print("Player just earned 5 points ")

# 5.4
alien_color = 'red'
if alien_color == 'green':
    print('You just earned 5 points for shooting the alien' )
else:
     print('You just earned 10 points' )

# 5.5
if alien_color == 'green':
    print('You just earned 5 points for shooting the alien' )
elif alien_color == 'yellow':
     print('You just earned 10 points' )
elif alien_color == 'red':
     print('You just earned 15 points' )

# 5.6
age = 65

if age < 2:
    stage ='baby'
elif age < 4:
     stage =' toddler'
elif age < 13:
     stage ='kid'
elif age < 20:
     stage ='teenager'
elif age < 65:
     stage ='adult'
elif age >=65:
     stage ='elder'

print(f"Amaka is a {stage}")

# 5.7

favourite_fruits =['bananas','apples','cherry','mango','strawbery','coconut']

fruit ='apple'
#  when we use multiple if ,it checks all condition,so everyline of code is executed,used when we want multiple condition to be true 
if 'apples' in favourite_fruits:
     print(f"You really like apples ")
if 'bananas' in favourite_fruits:
      print(f"You really like bananas ")
if 'pear' in favourite_fruits:
     print(f"You really like pear ")
if 'guava' in favourite_fruits:
     print(f"You really like guava ")
if 'mango' in favourite_fruits:
     print("You really like mango")

# but when we chain else statements the code stops running when any condidtion is met,can be used when we need one condition to just be true
if "apples" in favourite_fruits:
     print(f"You really like apples ")
elif 'mango' in favourite_fruits:
      print(f"You really like pear ")
elif 'pear' in favourite_fruits:
      print(f"You really like pear ")
else:
      print("You really like mango")
