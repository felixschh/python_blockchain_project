# 1): Write a normal function that accepts another function as an argument.
# Output the result of that other function in your normal function.
def trans_data(fn):
    print(fn(10))

# 2): call your "normal" function by passing a lambda function 
# - which performs any operation of your choice - as an argument
trans_data(lambda data: data / 5)

# 3): weak your normal function by allowing an infinite amout of arguments on 
# which your lambda function will be executed
def trans_data2(fn, *args):
    for arg in args:
        print(fn(arg))
    
trans_data2(lambda data: data / 5, 10, 15, 22, 30)



# 4): format the output of your "normal" function such that 
# numbers look nice and are centered in a 20 character column
def trans_data3(fn, *args):
    for arg in args:
        print('Result: {:20}'.format(fn(arg)))
trans_data3(lambda data: data / 5 ,10, 15,22, 30)