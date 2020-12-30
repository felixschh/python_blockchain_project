# defining our blockchain as an empty list
blockchain = []


# defining function that returns last blockchain value
def get_last_blockchain_value():
    return blockchain[-1]


# writing a function to add values to the blockchain
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


# invoke function
add_value(2)
add_value(0.9, get_last_blockchain_value())
add_value(10.89, get_last_blockchain_value())


print(blockchain)
