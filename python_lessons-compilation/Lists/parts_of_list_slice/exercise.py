programs_list =['dancing','refreshments','singing','exchange of vow','sharing of gifts']
print('The first three items on the list are :')
for program in programs_list[:3]:
    print(program.title())

print('Three items from  the middle of the  list are :')
for program in programs_list[1:4]:
    print(program.capitalize())

my_pizzas=['burito','Pepperoni','magarita','dominos']
friend_pizza = my_pizzas[:]
print(my_pizzas,'mine')
print(friend_pizza,'friend')
my_pizzas.append("veggies pizza")
friend_pizza.append("chocolate piza")

print ("My favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print ("My friends's favourite pizzas are:")
for pizza in friend_pizza:
    print(pizza)

# 4-12
my_foods =['pizza','falafel','carrot cake','ice cream','samosa']
print('Here are my favourite foods:')
for food in my_foods:
    print(food.upper())
friend_food = my_foods[:]
friend_food.append("smoothie")
friend_food.remove("falafel")
print('Here are my friends  favourite foods:')
for food in friend_food:
    print(food.title())