# defining our blockchain as an empty list
blockchain = []


# defining function that returns last blockchain value
def get_last_blockchain_value():
    return blockchain[-1]


# writing a function to add values to the blockchain
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

# refactoring
def get_user_input():
    return float(input('Your transaction amount please: '))


# invoke function with repetitive use of built-in input function
tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())


print(blockchain)
