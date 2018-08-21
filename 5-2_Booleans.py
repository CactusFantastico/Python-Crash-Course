#  conditional with a .lower fixer
name = 'Maxwell'
print("Is name == to 'maxwell'? I predict true")
print(name == 'maxwell')
print(name.lower() == 'maxwell')

#  conditional with an absolute value fixer
number = -1*34**12
print("is number == to " + str(34**12) + "?")
print(number == 34**12)
print(number.__abs__() == 34**12)

#  not a conditional but I could make it conditional...
if number == 34**12:
    print("cool, dude!")
elif number.__abs__() == 34**12 :
    print('Why is your shit negative, dawg?')
else:
    print('You done fucked up a-a-ron.')


