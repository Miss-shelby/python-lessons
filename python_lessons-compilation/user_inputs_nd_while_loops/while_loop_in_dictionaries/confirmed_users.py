#  A for loop is effective for looping through a list, but you shouldn’t modify 
# a list inside a for loop because Python will have trouble keeping track of the 
# items in the list. To modify a list as you work through it, use a while loop. 
# Using while loops with lists and dictionaries allows you to collect, store, and 
# organize lots of input to examine and report on later.


# NOTE: Moving Items from One List to Another
#  Consider a list of newly registered but unverified users of a website. After 
# we verify these users, how can we move them to a separate list of confirmed 
# users? One way would be to use a while loop to pull users from the list of 
# unconfirmed users as we verify them and then add them to a separate list of 
# confirmed users. Here’s what that code might look like:
unconfirmed_users=['alice','ngozi','brian','candice']
confirmed_users=[]


#  Verify each user until there are no more unconfirmed users.
 #  Move each verified user into the list of confirmed users.

#  so here while unconfirmed user list is not empty we loop through each user and assign it to the current user varible by using pop method which means we are removing the user one by one to verify them by assigning them to current_user varibale.
# Then we move the users to the confirmed users array 
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user:{current_user.title()}")
    confirmed_users.append(current_user)

print(unconfirmed_users,'previous unconfirmed users before confirming ')

# Display all confirmed users
print("\nThe folloing users have been confirmed:")
for c in confirmed_users:
    print(c.title())

# explanation

#  We begin with a list of unconfirmed users at u (Alice, Brian, and 
# Candace) and an empty list to hold confirmed users. The while loop 
# runs as long as the list unconfirmed_users is not empty. Within this loop, the 
# pop() function  removes unverified users one at a time from the end 
# of unconfirmed_users. Here, because Candace is last in the unconfirmed_users 
# list, her name will be the first to be removed, assigned to current_user, and 
# added to the confirmed_users list at x. Next is Brian, then Alice.
#  We simulate confirming each user by printing a verification message 
# and then adding them to the list of confirmed users. As the list of uncon
# f
#  irmed users shrinks, the list of confirmed users grows. When the list of 
# unconfirmed users is empty, the loop stops and the list of confirmed users 
# is printed: