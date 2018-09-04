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


print('Lets get started on our character! '
      'This program only handles numbers, so please use those when making your selection')
print('At any moment you can pick from one of the options listed or '
      'just enter 0(zero) to let the computer randomly decide.')

#  Gender picker
gender = input("""First, tell me if your character is a male or a female? 
-------------
| 0 | Random |
| 1 | Male   |
| 2 | Female |
-------------""")
if gender == 2:
    character['gender'] = 'Female'
if gender == 1:
    character['gender'] = 'Male'
else:
    gender = ['Male', 'Female']
    character['gender'] = random.choice(gender)
print('You are a {}.'.format(character['gender']))

#  Race picker
print('Lets pick a race. Choose the corresponding number for your race of choice:')
races = """ -------------
|Random   | 0 |
|Dwarf    | 1 |
|Elf      | 2 |
|Human    | 3 |
|Half-orc | 4 |
 -------------"""
race_picker = int(input(races))
if race_picker == 0:
    dice(dsize=4)
    print(rolls)
    race_picker = rolls.pop()
if race_picker == 1:
    character['race'] = 'Dwarf'
if race_picker == 2:
    character['race'] = 'Elf'
if race_picker == 3:
    character['race'] = 'Human'
if race_picker == 4:
    character['race'] = 'Half-orc'
print('You are a {} {}.'.format(character['gender'], character['race']))

#  Parents picker
parents = int(input("""Now, lets talk about your parents.
 --------------
 | 0      | r |
 | 01-95  | a |
 | 96-100 | b |
 --------------
 Please select the number of your choice: """))

if parents == 0:
    dice(dsize=100)
    print(rolls)
if parents >= 96:
    character['parents'] = 'doesn\'t know their parents'
else:
    character['parents'] = 'knows their parents'
print('You are a {} {} who {}.'.format(character['gender'], character['race'], character['parents']))
print(character)
print(rolls)
print(race_picker)

#  Half-orc parents module
if character['race'] == 'Half-orc':
    print("""Since you're a Half-orc, we need to establish what race your parents are.
    -----------
    | 0   | r |
    | 1-4 | a |
    | 5-6 | b |
    | 7   | c |
    | 8   | d |
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

#  Half-elf parents module
if character['race'] == 'Half-elf':
    print("""Since you're a Half-orc, we need to establish what race your parents are.
    -----------
    | 0   | r |
    | 1-4 | a |
    | 5-6 | b |
    | 7   | c |
    | 8   | d |
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

