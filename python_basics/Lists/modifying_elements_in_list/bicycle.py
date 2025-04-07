#list stands for array in js
bicycles =['trek','redline','cannondale']
print(bicycles)

#accesscing elements in a list,its 0 index e.g first item = bicycles[0]
print(bicycles[0])
print(bicycles[0].title())

#to access last item we use -1,second to last -2,third to last -3
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)