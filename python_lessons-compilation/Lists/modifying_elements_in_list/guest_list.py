guest_list =['Ngozi','imma','chioma','amanda']

mesaage = f"{guest_list[0]},you are highly invited to my dinner party "
mesaage_two = f"{guest_list[1]},you are highly invited to my dinner party "
mesaage_three = f"{guest_list[2]},you are highly invited to my dinner party "
mesaage_lst = f"{guest_list[-1]},you are highly invited to my dinner party "
print(mesaage,mesaage_two,mesaage_three,mesaage_lst)

cant_make_it_guest ='imma'
print(cant_make_it_guest)

guest_list[1] ='bay'
print(guest_list)

print(f'Hey {guest_list[0]},{guest_list[1]},{guest_list[2]},{guest_list[3]} i just found a bigger venue for the party at lekki')

guest_list.insert(0,'chichi')
guest_list.insert(1,'ada')
guest_list.append('Miriam')

print(f'New guest list:{guest_list}')

# shrinking guest list 
print (f'sorry loves:{guest_list[0]},{guest_list[1]},{guest_list[2]},{guest_list[3]},{guest_list[4]},{guest_list[5]},{guest_list[6]} I can  only invite two people.')
not_guest = guest_list.pop(0)

not_guest_a = guest_list.pop(1)
not_guest_b = guest_list.pop(2)
not_guest_c = guest_list.pop(3)
not_guest_d = guest_list.pop(-1)
print(f'sorry {not_guest.title()} You are uninvited')

print(f'sorry {not_guest_a.title()} You are uninvited')
print(guest_list)
print(f'sorry {not_guest_b.title()} You are uninvited')
print(guest_list)
print(f'sorry {not_guest_c.title()} You are uninvited')
print(guest_list)
print(f'sorry {not_guest_d.title()} You are uninvited')
print(guest_list)
print(f'Hey besties {guest_list[0]} and {guest_list[1]},you are still invited to my party')
del guest_list[0]
del guest_list[0]
print(guest_list,'oops')