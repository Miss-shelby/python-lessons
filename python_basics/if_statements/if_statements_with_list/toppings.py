
# watching specicial values in list 
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")
print("\nFinished making your pizza")

# But what if the pizzeria runs out of green peppers? An if statement 

for requested_topping in requested_toppings:
    if(requested_topping == 'green peppers'):
        print("Sorry,we are out of green peppers right now")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")

out_of_stock ='green peppers'
for requested_topping in requested_toppings:
    if(requested_topping == out_of_stock.lower()):
        print(f"Sorry,we are out of {out_of_stock.title()} right now")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")

# checking if a list is empty
requested_toppings =[]
if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}")
    print("Finished making your pizza ma")
else:
    print("Are you sure you want a plain pizza?")

# using multiple lists,we want to check if requested topping is in our available toppings
available_toppings =['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"We don't have {requested_topping}")