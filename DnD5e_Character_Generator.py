import random
rolls = []


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


def dice(dnumber =1, dsize =6):
    dice_size_picker(dx=dsize)
    for i in range(0,dnumber):
        rolls.append(random.randint(1,dsize))


number_of_dice = int(input("How many dice would you like to roll? "))
dice_picker = input("""what size dice would you like to roll?
    Choices are d2, d4, d6, d10, d12, and d20""")

dice_size = dice_size_picker(dx=dice_picker)
dice(dnumber=number_of_dice, dsize=dice_size )
print(rolls)