# height = input("How tall are you, in inches?")

# height =int(height)

# if height >= 48:
#     print("\nYou are tall enough to ride!")
# else:
#      print(f"\nYou'll be able to ride when you're  {48 - height} older.")

#  The Modulo Operator
#  A useful tool for working with numerical information is the modulo operator (%), 
# which divides one number by another number and returns only the remainder:

print(4%3)
print (4%2)

number = input("Enter a number,and i will tell you if its an even or odd number")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even")
else:
     print(f"\nThe number {number} is odd.")  