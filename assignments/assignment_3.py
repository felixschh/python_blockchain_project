# Create a list of "person" dictionaries with a name, 
# age and list of hobbies for each person. Fill in any data you want.
persons = [
    {
    'name': 'Luis', 'age': 26, 'hobbies': ['tennis', 'golf', 'cooking']},
    {
    'name': 'Felix', 'age': 23, 'hobbies': ['tennis', 'football', 'basketball']},
    {
    'name': 'Peter', 'age': 19, 'hobbies': ['gaming', 'running', 'reading']}
]
print(persons)
print('-' * 20)
print()

# Use a list comprehension to convert this list of persons into a list of names (of the persons)
names = [person['name'] for person in persons]
print(names)
print('-' * 20)
print()


# Use a list comprehension to check whether all persons are older than 20.
older_twenty = all([person['age'] > 20 for person in persons])
print(older_twenty)
print('-' * 20)
print()


# Copy the person list such that you can safely edit the name
# of the first person (without changing the original list)
copied_persons = [person.copy() for person in persons]
copied_persons[0]['name'] = 'Maximilian'
print(copied_persons)
print(persons)
print('-' * 20)
print()


# Unpack the persons of the original list into different variables and output these variables.
unpack = persons[:]
person1, person2, person3 = unpack 
print(person1)
print(person2)
print(person3)