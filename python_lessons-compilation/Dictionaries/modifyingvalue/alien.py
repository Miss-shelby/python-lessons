# dictionaries are objects in javascript,the keys must be in a stringe;e.g here color and points is key while green and 5 is the value

alien_0 ={'color':'green','points':5}
print(alien_0)

print(alien_0['color'])

# we can assign   dictionary value to a new variable below:
new_points = alien_0['points']
print(f"You have just earned {new_points} points!")

# //adding new key-value pair to dicitionary 
alien_0['x_position'] = 0
alien_0['y_position']=25
print(alien_0)
 
# starting with empty dictionary ,we can add value to it viz 
alien_1 = {}
alien_1['color'] ='pink'
alien_1['points'] = 10
print(alien_1)

# modifying values in dictionary 
alien_0 ={'color':'green'}
print(f"The alien is {alien_0['color']} in color")

alien_0['color']='orange'
print(f"The alien is now {alien_0['color']} in color")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium','points':5}
print(f"The original x position:{alien_0['x_position']}")

#move the alien to the right 
# determine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
    x_increament = 1
elif alien_0['speed'] == 'medium':
    x_increament = 2
else:
    # this must be a ver fast alien 
    x_increament = 3

# The new position is now determined with the speed
alien_0['x_position'] = alien_0['x_position'] + x_increament
print(f"The new x position: {alien_0['x_position']}")

# we can change one value in the dictionary and the overall behavious of the alien changes 
alien_0['speed'] = 'fast'

alien_0['x_position'] = alien_0['x_position'] + x_increament
print(f"The newest x position: {alien_0['x_position']}")

# removing and deleting key-value pair in dictionary;NOTE  the deleted key-value pair is removed permanently.
del alien_0['points']
print(alien_0)