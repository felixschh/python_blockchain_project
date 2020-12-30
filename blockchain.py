# defining our blockchain as an empty list
blockchain = [[1]]



# writing a function to add values to the blockchain
def add_value(transaction_amount):
    blockchain.append([blockchain[-1], transaction_amount])
    print(blockchain)



# invoke function
add_value(2)
add_value(0.9)
add_value(10.89)

