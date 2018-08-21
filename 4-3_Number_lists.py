# 4-3 counting to 20
for number in range(1, 21):
    print(number)

# 4-4 comprehension list counting to a million
million = [value for value in range(1, 1000001)]

print(len(million))
print(max(million))
print(min(million))
print(sum(million))  # 4-5

# 4-6 counting odds
odds = []
for odd in range(1, 20, 2):
    odds.append(odd)
    print(odd)

# 4-7 counting by threes
for triples in range(3, 31, 3):
    print(triples)

# 4-8 append and print a list of cubes 1-10
cubes = []
for cube in range(1,11):
    cubes.append(cube**3)
    print(cube**3)
print(max(cubes))
print(min(cubes))

# 4-9 list comprehension of cubes 1-10
cubecomp = [cubec**3 for cubec in range(1, 11)]
print(max(cubecomp))
print(min(cubecomp))
