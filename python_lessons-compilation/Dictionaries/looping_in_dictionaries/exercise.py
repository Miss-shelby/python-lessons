rivers = {
'nile':'egypt',
'niger':'nigeria',
'misippipi':'usa'
}

for river,country in rivers.items():
    print(f"The {river} runs through {country}")

for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'ammie':'javascript',
    'nk':'c'
}
friends=['ng','ben','ammie','jen']

for name in favorite_languages:
    if name in friends:
        language=favorite_languages[name]
        print(f"{name.title()} Thank you for choosing {language} as your fav languge")
    else:
        print(f"{name} please take the poll.")