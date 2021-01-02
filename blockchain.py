# defining our blockchain as an empty list
blockchain = []


# defining function that returns last blockchain value
def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# writing a function to add values to the blockchain
def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchainvalue to the blockchain
    Arguments:
    :transaction_amount: The amount should be added.
    :last_transaction: The last blockchain transaction (default[1]).
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


# function to get the users input of the amount of transaction
def get_transaction_value():
    return float(input('Your transaction amount please: '))

# function to receive users choices of inputs
def get_user_choice():
    return input('Your choice: ')

# Output the blockchain list to console
def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)


while True:
    """ Printing out the different input options """
    print('Please choose:')
    print('1: Add a new transacion value')
    print('2: Output the blocks of the blockchain')
    print('q: Quit')
    """ receiving users choice """
    user_choice = get_user_choice()
    """ unsing conditions to invoke functions depending on users input """
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list!')
    print('Choice registered!')  


print('Done!')