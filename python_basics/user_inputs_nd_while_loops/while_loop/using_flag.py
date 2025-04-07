# For a program that should run only as long as many conditions are true, 
# you can define one variable that determines whether or not the entire pro
# gram is active. This variable, called a flag, acts as a signal to the program. We 
# can write our programs so they run while the flag is set to True and stop run
# ning when any of several events sets the value of the flag to False. As a result, 
# our overall while statement needs to check only one condition: whether or 
# not the flag is currently True. Then, all our other tests (to see if an event has 
# occurred that should set the flag to False) can be neatly organized in the rest 
# of the program.

# prompt='Tell me sth and i will repeat it back to you'
# prompt += "\nEnter 'quit' to end the program. "
# active = True

# while active:
#     message =input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

#  Using break to Exit a Loop
#  The break statement lets you exit a loop when the condition is met.
#  This is useful when you want to exit a loop based on user input or other
# prompt ='\nPlease enter the name of a city you have visited: '
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'D Love to go to {city.title()}")

# using continue in a loop 
# The continue statement tells Python to skip the current iteration of a loop
# and move on to the next iteration. This is useful when you want to skip over
# certain values in a loop without exiting the loop entirely. For example, if you   
# want to skip over even numbers in a loop, you can use the continue statement to
# skip them and continue with the next iteration.
current_number =0
while current_number < 10:
    current_number +=1
    if current_number % 2 == 0:
        continue
    print(current_number)

