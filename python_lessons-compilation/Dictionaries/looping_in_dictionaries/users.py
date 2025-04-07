user_0 ={
    'username':'efermi',
   ' first':'enrico',
   'last':'fermi'
}
# to loop we create names for two varibales that will hold key and value,followed by method items()

for key,value in user_0.items():
    print(f"\nKey :{key}") 
    print(f"\nValue: {value}")



favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'ammie':'javascript',
    'nk':'c'
}

for name,language in favorite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")
# to get only keys 
for name in favorite_languages.keys():
    print(name.title())

# You can access the value associated with any key you care about inside 
# the loop by using the current key. Let’s print a message to a couple of friends 
# about the languages they chose. We’ll loop through the names in the diction
#  ary as we did previously, but when the name matches one of our friends, we’ll 
# display a message about their favorite language

friends =['phil', 'sarah']



# to check if the name is contained in friends dictionary  then use it to print their language 
for name in favorite_languages.keys():
    print(name.title(),'names ')
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()},i see you love {language}")

# to check if a prticluar friend/person didnt take the pull 
if 'erin' not in favorite_languages.keys():
    print("Erin,please take the poll!")

#  Looping Through a Dictionary’s Keys in a Particular Order
# we use sorted() to sort our list in alphabetical order before looping 
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()},thank you for taking the poll.")

# Looping Through All Values in a Dictionary
for lan in favorite_languages.values():
    print(lan.title())
# This approach pulls all the values from the dictionary without checking 
# for repeats. That might work fine with a small number of values, but in a 
# poll with a large number of respondents, this would result in a very repeti
#  tive list. To see each language chosen without repetition, we can use a set. 
# A set is a collection in which each item must be unique:

# When you wrap set() around a list that contains duplicate items, Python 
# identifies the unique items in the list and builds a set from those items.
for lan in set(favorite_languages.values()):
    print(f"\n{lan.title()} fav language in a set ")

#  The result is a nonrepetitive list of languages that have been mentioned 
# # by people taking the poll