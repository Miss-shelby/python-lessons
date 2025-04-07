#  Filling a Dictionary with User Input

responses ={}
# responses['Ammie'] ='I love food'

print(responses)
 # Set a flag to indicate that polling is active
polling_active = True
while polling_active:
      # Prompt for the person's name and response
        #   save the users name in the name varible and response in the 'response' variable
      name = input("\nWhat is your name? ")
      response = input("Which mountain would you like to climb someday? ")
        # Store the response in the dictionary.
      responses[name] = response

       # Find out if anyone else is going to take the poll.
      repeat = input('would you like to let another person respond? (yes/no) ')
      if repeat == 'no':
            print(repeat,'repeat here ')
            polling_active = False

 # Polling is complete. Show the results
for name,response in responses.items():
      print(f"{name.title()} would like to climb {response.title()}")