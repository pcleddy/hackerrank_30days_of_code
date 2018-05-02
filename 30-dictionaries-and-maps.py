import sys

entries = input().strip()
phonebook = {}
for entry in range(int(entries)):
    name, phone = input().strip().split(' ')
    phonebook[name] = phone

for line in sys.stdin:
    name = line.strip()
    if name not in phonebook:
        print('Not found')
    else:
        print(name + '=' + phonebook[name])

    