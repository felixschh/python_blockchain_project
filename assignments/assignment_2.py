# Create a list of names and use a for loop to output the length of each name (len())
names = ['Susanne', 'Felix', 'Louise', 'Luis', 'Reinhold', 'Nadine']

print()
print('Excercise 1: ')

for name in names:
    print(name + ' - ' + str(len(name)))

# Add an if check inside the loop to only output names longer than 5 characters.
print()
print('Excercise 2: ')
for name in names:
    if len(name) > 5:
        print(name + ' - ' + str(len(name)))


# Add another if check to see wheter a name includes a 'n' or 'N' character.
print()
print('Excercise 3: ')
for name in names:
    if len(name) > 5:
        if ('n' or 'N') in name:
            print(name + ' - ' + str(len(name)))

# Use a while loop to empty the list of names (pop()).
print()
print('Excercise 4: ')

while len(names) > 0:
    names.pop()
    print(names)