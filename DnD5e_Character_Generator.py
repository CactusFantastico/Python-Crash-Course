import random
rolls = []
character = {}


def dice_size_picker(dx):
    if dx == 'd2':
        return 2
    if dx == 'd4':
        return 4
    if dx == 'd6':
        return 6
    if dx == 'd8':
        return 8
    if dx == 'd10':
        return 10
    if dx == 'd12':
        return 12
    if dx == 'd20':
        return 20
    if dx == 'd100':
        return 100


def dice(dnumber=1, dsize=6):
    dice_size_picker(dx=dsize)
    for i in range(0, dnumber):
        rolls.append(random.randint(1, dsize))


print('Lets get started on our character!')
print('At any moment you can pick from one of the options listed or '
      'just press enter to let the computer randomly decide.')

#  Gender picker
gender = input('First, tell me if your character is a male or a female? ')
if gender.lower() == 'female':
    character['gender'] = 'Female'
if gender.lower() == 'male':
    character['gender'] = 'Male'
else:
    gender = ['Male', 'Female']
    character['gender'] = random.choice(gender)
print('You are a {}.'.format(character['gender']))

#  Race picker
print('Lets pick a race. Choose the corresponding letter for your race of choice:')
races = """ _____________
|Dwarf    | 1 |
|Elf      | 2 |
|Human    | 3 |
|Half-orc | 4 |
 _____________"""
race_picker = input(races)
if race_picker == '':
    dice(dsize=4)
    race_picker = str(rolls.pop())
if race_picker == '1':
    character['race'] = 'Dwarf'
if race_picker == '2':
    character['race'] = 'Elf'
if race_picker == '3':
    character['race'] = 'Human'
if race_picker == '4':
    character['race'] = 'Half-orc'
print('You are a {} {}.'.format(character['gender'], character['race']))

#  Parents picker
parents = input('Now, lets talk about your parents. A or B? ')
if parents == '':
    dice(dsize=100)
    print(rolls)
    if rolls.pop() >= 96:
        parents = 'b'
    else:
        parents = 'a'
if parents.lower() == 'b':
    character['parents'] = 'doesn\'t know their parents'
if parents.lower() == 'a':
    character['parents'] = 'knows their parents'
print('You are a {} {} who {}.'.format(character['gender'], character['race'], character['parents']))
print(character)
print(rolls)
print(race_picker)

#  Racial parents module
if character['race'] == 'Half-orc':
    print("""Since you're a Half-orc, we need to establish what race your parents are.
    -----------
    | 1-4 | a |
    | 5-6 | b |
    | 7   | c |
    | 8   | d |
    | 0   | r |
    ------------""")
    racial_parents = int(input("Please select the corresponding number of your choice"))
    if racial_parents == 0:
        dice(dsize=8)
        print(rolls)
        racial_parents = rolls.pop()
        print(racial_parents)
    if racial_parents <= 4:
        character["Parent Race"] = "a"
    if racial_parents <= 6:
        character["Parent Race"] = "b"
    if racial_parents == 7:
        character["Parent Race"] = "c"
    else:
        character["Parent Race"] = "d"
print(character)