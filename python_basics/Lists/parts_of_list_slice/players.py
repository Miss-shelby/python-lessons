
# we use slice to cut out part of a list,specify start and end index 
players =[
 'ronald',
 'micheal',
 'florence',
 'eli',
 'charles'
]
print(players[0:3],'players from index 0 to 3')
print(players[1:4],'players from index 1 to 4')
# If you omit the first index in a slice, Python automatically starts your 
# slice at the beginning of the list
print(players[:3],'players from index 0 to the third ')

# if you omit the last,it starts slice from the index you specified down to the last item
print (players[3:],'players from index 3 to the last ')

# looping through slice 
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print("Here are the first three plyers on my team:")
for player in players[:3]:
    print(player.title())

# copying  a list 

# to create  a copy we use [:] with no start or ending index which means copy the whole list 
my_foods =['pizza','falafel','carrot cake']
friends_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)
print("\nMy Friends fav foods are :")
print(friends_foods)

my_foods.append("cannoli")
friends_foods.append("ice cream")
print("My favorite foods are:")
print(my_foods)
print("\nMy Friends fav foods are :")
print(friends_foods)
