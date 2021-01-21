import random
import datetime
print('')
print('')
# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10
def rn1():
    rn = random.random()
    return rn

def rn2():
    rn = random.randint(0, 10)
    return rn

print(rn1())
print(rn2())
print('')


# 2) Use the datetime library together with the random number to generate a random, unique value
def dt():
    dt_num = str(datetime.datetime.now()) + str(random.randrange(0, 101))
    return dt_num

print(dt())
