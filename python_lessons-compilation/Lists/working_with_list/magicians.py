#  for loop in list 

clowns =['twyse','maraji','lasisi','layi','taoma']
for clown in clowns:
    print(clown)

for clown in clowns:
    print (f"{clown.title()},i enjoy your contents ")
    print(f"I can't wait to see your next content, {clown.title()}.\n")
# The identation shows the for loop ,the msg below is outside the forloop
print('Thank you everyone for the great show ')

fruits =['mango','apple','kiwi','orange']
for fruit in fruits:
    print(fruit)
    print(f"I love {fruit.title()}")
    print(f"I love these fruits {fruit.title()} equally")
print(f"I can't wait to restock on; {fruit.title()}.\n")
