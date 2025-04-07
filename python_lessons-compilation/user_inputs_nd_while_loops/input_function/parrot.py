#  The input() function pauses your program and waits for the user to enter 
# some text. Once Python receives the user’s input, it assigns that input to a 
# variable to make it convenient for you to work with.

message = input("Tell me somethig, and i will repeat it back to you:")
# print(message)

# The input() function takes one argument: the prompt, or instructions, 
# that we want to display to the user so they know what to do. In this example, 
# when Python runs the first line, the user sees the prompt Tell me something, 
# and I will repeat it back to you: . The program waits while the user enters 
# their response and continues after the user presses enTer. The response is 
# assigned to the variable message, then print(message) displays the input back to 
# the user
name = input("Please enter your name")
# print(f"\nHello, {name}")

prompt = "If you tell us who you are, we can personalise the message you see"
prompt += "\nWhat is your first name"

name = input(prompt)
# print(f"\nHello, {name}")

# we use int() when we want to get number from user,python treats input as string

age = input("How old are you?")
print(age)
# convert age to number using int 
age = int(age)
print(age >= 18)