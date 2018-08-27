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
gender = input('First, tell me if your character is a boy or a girl? ')
if gender.lower() == 'girl':
    character['gender'] = 'girl'
if gender.lower() == 'boy':
    character['gender'] = 'boy'
else:
    gender = ['boy', 'girl']
    character['gender'] = random.choice(gender)

#  Race picker
print('Lets pick a race. Choose the corresponding letter for your race of choice:')
races = """Dwarf - a
Elf - b
Human - c
Half-orc - b"""
race_picker = input(races)
if race_picker == '':
    dice(dsize=4)
    race_picker = rolls
if race_picker == '1':
    character['race'] = 'Dwarf'
if race_picker == '2':
    character['race'] = 'Elf'
if race_picker == '3':
    character['race'] = 'Human'
if race_picker == '4':
    character['race'] = 'Half-orc'

#  Parents picker
parents = input('Now, lets talk about your parents. A or B? ')
if parents.lower() == 'a':
    character['parents'] = 'a'
if parents.lower() == 'b':
    character['parents'] = 'b'
else:
    dice(dsize=100)
    print(rolls)
    if rolls.pop() >= 96:
        character['parents'] = 'b'
    else:
        character['parents'] = 'a'
print(character)
print(rolls)
