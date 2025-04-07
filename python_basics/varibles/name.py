# defining strings in python

name ='ada agu'
# title() takes in empty parentheses and its used to capitalise each word,will return Ada Agu in this case 
print(name.title())

# use f to contenate strings like template literal in js 
first_name ='Ammie'
last_name = 'Baby '

full_name = f"{first_name} {last_name}"

print(full_name)
message = (f"Hello {full_name.title()},you are welcome  ")
print(message)

# to add white spaces to your text use \t
print("\tpython")

# printing text in new lines \n
print("my favourite languages:\npython,\njavascript,\nphp")

# use rstrip() to remove white spaces from right and lstrip() to remove from left and strip() to remove from both sides

left_space ='   i have left space'
print(left_space)

left_space = left_space.lstrip()
print(left_space)

both_side_spaces ='  i have spaces on both sides  '
both_side_spaces = both_side_spaces.strip()
print(both_side_spaces)

# avoiding apostrophe error
message ="One of python's strength is its diverse community"
print(message)