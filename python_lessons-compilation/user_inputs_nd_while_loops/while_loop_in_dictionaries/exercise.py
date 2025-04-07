# 7-8
sandwich_orders = ['cuban sandwich', 'pastrami sandwich','monte-cristo sandwich','elvis sandwich','pastrami sandwich','panuozzo sandwich','sirloin -steak sandwiches','pastrami sandwich','tuna sandwich','pastrami sandwich']

finished_sandwiches =[]
for sandwich in sandwich_orders:
    print(f"I made your {sandwich.title()}")
    finished_sandwiches.append(sandwich)

print("\nSandwiches that has been made are:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

# 7-8
print('Deli has run out of pastrami sandwich')
while 'pastrami sandwich' in finished_sandwiches:
    finished_sandwiches.remove("pastrami sandwich")

print("\nNew Deli available sandwiches are:")
for s in finished_sandwiches:
    print(s,'available')

# 7-10. Dream Vacation: 
dream_vacations={}

active = True
while active:
    name = input('what is your name baby? ')
    place= input(" If you could visit one place in the world, where would you go? ")
    print('Thanks for your response')
    dream_vacations[name] = place

    repeat = input("would you like to take another response.? (yes/no) ")
    if repeat == 'no':
        active = False
    # active = False


# print result 
for n,p in dream_vacations.items():
    print(f"{n.title()} would love to visit {p.title()}")