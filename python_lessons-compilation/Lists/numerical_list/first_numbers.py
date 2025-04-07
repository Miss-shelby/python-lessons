
# we use range() to generate series of numbers,code below print 1-4
for value in range(1,5):
    print(value)

for n in range(11):
    print(n)
# we can use list() to convert range of numbers into a list 
numbers = list(range(1,11))
print(numbers)

# when we pass a 3rd argument it uses a step value,ie how many numbers it will skip while generating the numbers 
even_numbers = list(range(2,11,2))
print(even_numbers)

squares =[]
for value in range(1,11):
    square= value ** 2
    squares.append(square)
print(squares)
# or 

for value in range(1,11):
    squares.append(value ** 2)
print(squares,'squares array')

# simple statistics with a list of numbers 
digits = [1,2,3,4,5,6,7,8,9,0]
# to get the smallest we use min(),biggest:max() and sum with sum()
print(min(digits))
print(max(digits))
print(sum(digits))

# A list comprehension combines the 
# for loop and the creation of new elements into one line, and automatically 
# appends each new element.

squres_list =[value ** 2 for value in range(1,11)]
print(squres_list)
# sqaure_list_two =  [ value in range(0,7)]
# print(sqaure_list_two)

