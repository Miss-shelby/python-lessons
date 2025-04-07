motorcyles= ['honda', 'yamaha', 'suzuki']
print(motorcyles)

# changing the value of fist element 
motorcyles[0] ='ducati'
print(motorcyles)

# we use append to add item to the end of the list
motorcyles.append('ducati')
print(motorcyles)

motorcyles = []
print(motorcyles)
print(motorcyles.append('honda'))
print(motorcyles.append('yamaha'))
print(motorcyles.append('suzuki'))
print(motorcyles)

# insert adds item to the list at position specified,it dosent delete the existing element on that list 
motorcyles.insert(0,'ducati')
print(motorcyles)

# we use del to remove item at a particluar index or position 
del motorcyles[0]
print(motorcyles)

# we use pop() to remove the last item in a list and it allows us to store/access the removed item 

popped_motorcyle = motorcyles.pop()
print(popped_motorcyle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print (f'The last bike i owned was a {last_owned.title()}.')

# we can also specify the index/position which we want to pop an item 

first_owned = motorcycles.pop(0)
print(f"the fist bike i owned was a {first_owned.upper()}")

# we remove an item by value if we know the value of the item  using remove() method and passing the value in the parantheses

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
      
motorcycles.remove('yamaha')
print(motorcycles)

too_old ='ducati'
motorcycles.remove(too_old)
print(motorcycles)

print(f"\nA {too_old.title()} is too old and bland for me")

# The remove() method deletes only the first occurrence of the value you specify. If there’s 
# a possibility the value appears more than once in the list, you’ll need to use a loop 
# to make sure all occurrences of the value are removed. You’ll learn how to do this in 
# # Chapter 7