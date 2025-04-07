places_to_visit =['maldives','sychelles','zanzibar','kenya','dubai','canada']
print(places_to_visit)

print(sorted(places_to_visit))
print(places_to_visit,'orginal list')

print(sorted(places_to_visit,reverse=True))
print(places_to_visit,'orginal list')

places_to_visit.reverse()
print(places_to_visit,'after reverse')

places_to_visit.reverse()
print(places_to_visit,'back to original state ')

places_to_visit.sort()
print(places_to_visit,'after sorting')

message = f"The number of places on my bucket list is {len(places_to_visit)}"
print(message)

hobbies =['reading','music','writing','dancing','good time']
print(hobbies)
print(hobbies[0].title())
print(len(hobbies))
hobbies.insert(2,'eating')
print(hobbies)