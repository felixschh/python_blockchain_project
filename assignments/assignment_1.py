#1 create two variables - one with your age and one with your name
name = 'Felix '
age = 23


#2 create a function which prints your data as one string
def print_name_age(name, age):
    print(name + str(age) )


#3 create a function which prints any data (two arguments) as one string
def print_any_data():
    arg1 = str(input('type in your first string: '))
    arg2 = str(input('type in your second string: '))
    print(arg1 + arg2)

# 4 create a function which calculates and returs the nubmer of decades you lived
def print_decade_calculator():
    age = int(input('please type in your age: '))
    age = str(age)
    print(age[0])
    return age[0]
    


print_name_age(name, age)

print_any_data()

print_decade_calculator()

