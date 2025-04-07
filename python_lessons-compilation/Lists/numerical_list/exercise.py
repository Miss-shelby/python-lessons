# 4.3
for n in range (1,21):
    print (n)
# 4.4
one_million= [value for value in range(0,1000000)]
# print(one_million)
# 4.5
print(min(one_million),'min value')
print(max(one_million),'max value')
print(sum(one_million),'sum value')

# 4.6
for odd in range (1,20,2):
    print(odd,'odd numbers ')

# 4.7 : Make a list of the multiples of 3 from 3 to 30. Use a for loop to 
# print the numbers in your list
multiples_of_three = [ value**3 for value in range (3,31) ]
print(multiples_of_three,'3 multiples')

# 4.8
# cubes =[]
# for value in range(1,11):
#     cube = value **3
# cubes.append(cube)
# print(cubes,'cubes ')
cubes =[]
for value in range(1,11):
    cube = value **3
    print(cube )

# 4.9 using list comprehension
first_ten_cubes = [value**3 for value in range(1,11)]
print(first_ten_cubes)