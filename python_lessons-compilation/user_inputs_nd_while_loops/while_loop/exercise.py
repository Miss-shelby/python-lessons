prompt ='Enter your favourite pizza topping: '
prompt += 'Type "quit" to exist the program: '

# topping =  ''
# while  topping != 'quit':
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"Adding {topping.title()} to your pizza")
# print("Finished making your pizza!")  

# movie tickets
# prompt ='Enter your age '
# check = True 
# while check:
#     age = int(input(prompt))
#     if age < 3:
#         print('The ticket is free')
#     elif age >= 3 and age <=12:
#         # check = False
#         print('The ticket is $10')
#     else:
#         print('The ticket is $15')

topping =''
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        # break
        active = False
    else:
        print(f" {topping.title()} has been added to your pizza")