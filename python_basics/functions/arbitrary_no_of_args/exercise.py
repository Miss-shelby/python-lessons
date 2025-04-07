# 8-12
def make_sandwiches(*ingredients):
    print("\nList of items i want on my sandwich:")
    for i in ingredients:
        print(f"-{i}")
make_sandwiches('cheese')
make_sandwiches('pepper','extra cheese','flour')

# 8-13
def build_profile(first,last,**user_info):
    user_info['first'] = first
    user_info['last'] = last
    return user_info

user_profile = build_profile('ammie','tee',age=25,location='nigeria')
# print(user_profile)

my_profile = build_profile('mary','cynthia',age=26,hobby='reading',complexion='fair')
print(my_profile)

# 8-14
def make_car(manufacturer,model_name,**car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info
car = make_car('mercedez','lexus 350',color='midnight blue', year='2005')
print(car)
