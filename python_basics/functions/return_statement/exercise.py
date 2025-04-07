def city_country(city,country):
    full_country_name = f"{city} {country}"

    return full_country_name.title()

fav_place = city_country("santiago","chile")
fav_place_two = city_country("manchester","united kingdom")
print(fav_place)
print(fav_place_two)

# 8-7
def make_album(artist_name,album_title,number_of_songs =None):
    music_album = {'artist_name' : artist_name, 'album':album_title}
    if number_of_songs:
        music_album['tracks_number'] = number_of_songs
    

    return music_album

album_one = make_album('nastyC','strings and blings')
print(album_one)
album_two = make_album('posty','austin')
print(album_two)

album_three = make_album("drake","one dance",4)
print(album_three)

#  8-8. User Albums:
while True:
    print("\nEnter album description,type 'q' to quit the program")
    name= input("Enter the artist name  ")

    if name == 'q':
        break
    title = input ("Enter the album's title ")
    if title == 'q':
        break

    user_album = make_album(name,title)
    print(user_album,'user custom album')