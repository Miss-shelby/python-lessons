# we use tuple to create  a list that cannot change,they are immutable
#we define it just like list but use parantheses instaed
dimesions =(200,50)
print(dimesions[0])
print(dimesions[1])

# dimesions[0] = 250 //cant be reassigned 
# defining one tuple,must have a trailing comma 
my_t =(3,)
print(my_t)

# looping works same way as in list 
for d in dimesions:
    print (d)

# we can override a tupple viz 
original_top_three =('drake','kendrick','jcole')
print("Original top three artists are :")
for artist in original_top_three:
    print(artist.upper())

# overriding
original_top_three =('nastyc','posty','travis')
print("\nModified top three artists are :")
for artist in original_top_three :
    print(artist.title())