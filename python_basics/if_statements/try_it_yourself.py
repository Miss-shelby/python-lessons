# 5.8
user_names =['admin',"norman",'ammie','tee','cy']

for user in user_names:
    if user=='admin':
        print(f"Hello {user} would you like to see a status report?")
    else:
        print(f"Hello {user.title()},thank you logging in again")
# 5.9
user_names =[]
if user_names:
    for user in user_names:
        print(f"Hello {user}")
else:
    print(f"We need to find some users ")

# 5.10
current_users =['angel','GIFT','mary','black','ben']
new_users=['black','danny','GIFT','mascot','gaze']

# we use list comprehensuion we want to modify each element in a list 
current_users_lower = [user.lower() for user in current_users]
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"\n{user} username has been taken,try another ")
    else:
        print(f"{user} username is available")

# 5-11 ordinal number 

numbers =[1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(f"\n{number}st")
    elif number == 2:
        print(f"\n{number}nd")
    elif number == 3:
        print(f"\n{number}rd")
    else:
        print(f"\n{number}th")

# NOTE:
# In a loop (for), if-elif-else runs for each iteration, checking conditions separately.
# Without a loop, if-elif-else runs once and stops at the first True condition.