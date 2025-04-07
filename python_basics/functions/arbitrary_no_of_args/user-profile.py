#  NOTE:Using Arbitrary Keyword Arguments

# Sometimes you’ll want to accept an arbitrary number of arguments, but you 
# won’t know ahead of time what kind of information will be passed to the 
# function. In this case, you can write functions that accept as many key-value 
# pairs as the calling statement provides. One example involves building user 
# profiles: you know you’ll get information about a user, but you’re not sure 
# what kind of information you’ll receive. The function build_profile() in the 
# following example always takes in a first and last name, but it accepts an 
# arbitrary number of keyword arguments as well:used in creating dictionaries

# so baically we **kwargs when we want to create an empty didctionary that will aceept unlimited number of key-value pairs in a function and we use just *args when we want to pass multiple arguments that are not key value pairs  

def build_user_profile(first,last,**user_info):
    user_info['first'] = first
    user_info['last'] = last
    return user_info

user_profile = build_user_profile('ammie','tee',age=25,location='nigeria')
print(user_profile)

def build_store_products(**product_info):
    return product_info

products= build_store_products(product_name ='mosturizer',price = '#40,000', available =True)
print(products)