
emmah={
    'first_name':'ngozi',
    'last_name':'emma',
    'age':40,
    'city':'Awka'
}
print(emmah)
# 6.2 peoples fav numbers 
fav_numbers ={
    'nekky':3,
    'kay':7,
    'vics':10,
    'nahzy':5,
    'benny':2
}
print(f"Nekkys favourite number is {fav_numbers['nekky']}")

# 6.3
glossary={
    'list':'collection of item',
    'loop':'looping through items',
    'dictionary':'collection of key value pairs'
}
for word, meaning in glossary.items():
    print(word,meaning)
print(glossary)