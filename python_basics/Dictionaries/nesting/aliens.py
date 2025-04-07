alien_0 ={'color':'green','points':5}
alien_1 ={'color':'yellow','points':10}
alien_2 ={'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)
   
#  A more realistic example would involve more than three aliens with 
# code that automatically generates each alien. In the following example we 
# use range() to create a fleet of 30 aliens:

aliens =[]
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

# for alien in aliens:
#     # print(alien)
for alien in aliens[:5]:
    print(alien,'first five ')
print(f"Total number of aliens: {len(aliens)}")
# For example, to change the first three aliens to yellow, mediumspeed aliens worth 10 points each, we 
# could do this
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color']='yellow'
        alien['speed'] ='medium'
        alien['points']=20
    elif alien['color'] == 'yellow':
        alien['color'] ='red'
        alien['speed'] ='fast'
        alien['points'] = 14
    print(alien,'modidfied alien')

for alien in aliens:
    print(alien,'original alien')

#  A List in a Dictionary
#  Store information about a pizza being ordered.
pizza ={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}
print(f"You ordered a {pizza['crust']} with the following toppings:{pizza['toppings']}")

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t + {topping}")

favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name,languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favourite languages are :")
    else:
         print(f"\n{name.title()}'s favourite language is :")
    for language in languages:
        print(f"\t{language.title()}")

#  A Dictionary in a Dictionary
users ={
    'nokafor':{
        'first':'ngozi',
        'last':'okafor',
        'location':'manchester'
    },
    'yprincewill':{
        'first':'yagazie',
        'last':'princewill',
        'location':'canada'
    }
}

for username,user_info in users.items():
    print(f"\nUsername: {username}")
    # print(user_info)
    full_name = f"{user_info['first']} {user_info['last']}"
    location=f"{user_info['location']}"

    print(f"\tfull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")