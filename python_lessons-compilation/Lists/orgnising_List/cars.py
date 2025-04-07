# we use sort() to sort list elements alphabetically 

cars =['bmw','audi','toyota','corolla','peugot']
cars.sort()
print(cars)

# to sort in a reversed order we pass reverse = True as argument so it sorts in reverse alphabeticl order,again this order is permanently changed 

cars.sort(reverse=True)
print(cars)

# we used sorted function to preserve the original list   and perfom temporal sort 
print(f'Here is original list:{cars}')

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# sorted also take argument reverse = True 
# print(sorted(cars(reverse=True)))

#  Sorting a list alphabetically is a bit more complicated when all the values are not in 
# lowercase. There are several ways to interpret capital letters when determining a sort 
# order, and specifying the exact order can be more complex than we want to deal with 
# at this time. However, most approaches to sorting will build directly on what you 
# learned in this section

# we use reverse() method  to reverse the list order 
cars =['bmw','audi','corola','gle','lexus','toyota']
print(cars)

cars.reverse()
print(cars)

# finding the length of list 
print(len(cars))
