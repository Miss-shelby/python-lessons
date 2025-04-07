
# we can also use dictionary to store one kind of info about many objects

favourite_languages ={
    'jen':'python',
    'sarah':'c',
    'david':'django',
    'Ammie':'python',
}

sarah_lan = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {sarah_lan}")

# using get() to access dictionary values,the get method requires two argument;first is the key of the value you are getting and optionally the second argument is the value to be returned if the key dosent exist 
mary_lan = favourite_languages.get('mary','no language assigned ')
print(mary_lan)

# If the key 'points' exists in the dictionary, you’ll get the corresponding value. If it doesn’t, you get the default value. In this case, points doesn’t 
# exist, and we get a clean message instead of an error

#NOTE 
# If you leave out the second argument in the call to get() and the key doesn’t exist, 
# Python will return the value None. The special value None means “no value exists.” 
# This is not an error: it’s a special value meant to indicate the absence of a value. 
# You’ll see more uses for None in Chapter 8
mary_lan = favourite_languages.get('mary')
print(mary_lan)