guest_list = ['max', 'shawn', 'jeff', 'josh']
print('We cordially invite ' + ', '.join(guest_list) + ' to the party at our house')
print(guest_list[3].title() + ' cannot join us this evening.')
guest_list[3] = 'j.d'
print('We now are pleased to welcome ' + guest_list[3] + ' to the party')
print('A new table has been found!')
guest_list.insert(0, 'troy')
guest_list.insert(2, 'erik')
guest_list.append('jon')
print('We now welcome ' + ' and '.join(guest_list) + ' to the dinner party!')
for elem in guest_list[1:-1]:
    pop_guest = guest_list.pop()
    print(pop_guest + ' can no longer join us this evening.')
print('Unfortunately,' + ' and '.join(guest_list) + ' will be the only ones having dinner this evening.')
