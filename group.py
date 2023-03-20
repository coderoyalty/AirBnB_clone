#!/usr/bin/python3
from random import randint


admin_names = [
    "Royalty",
    "Abdullah",
    "Ovo Emmanuel",
    "Ilori",
]

names = [
    "Gloria",
    "Caroline",
    "Idara",
    "Stanley",
    "Taiwo",
    "nelson",
    "Richards",
    "onaya",
]

groups = [[], [], [], []]

group_size = int( (len(names) + len(admin_names)) / len(groups) )

# place admins in seperate groups
while len(admin_names):
    rand_pos = randint(0, group_size)
    rand_name = randint(0, len(admin_names) - 1)
    person = admin_names[rand_name]
    group = groups[rand_pos]
    if len(group) != 1:
        groups[rand_pos].append(person)
        admin_names.remove(person)


while len(names):
    rand_pos = randint(0, group_size)
    rand_name = randint(0, len(names) - 1)
    person = names[rand_name]
    group = groups[rand_pos]
    if len(group) != 3:
        groups[rand_pos].append(person)
        names.remove(person)

group_id = 'A'
for group in groups:
    print(f'---- group {group_id} ----')
    for member in group:
        print(member)
    group_id = chr(ord(group_id) + 1)
