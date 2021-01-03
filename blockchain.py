# defining our blockchain as an empty list
genesis_block = {
    'previous_hash': '',
    'index': 0, 
    'transaction': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Max'
participants = {'Max'}

# defining function to mine a block from open transactions
def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

# defining function that returns last blockchain value
def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# writing a function to add ne values to the blockchain
def add_transaction(recipient, sender=owner, amount=1.00):
    """ Append a new value as well as the last blockchainvalue to the blockchain
    Arguments:
    : Sender of the coins
    : Recipient of the coins
    : Amount of the coins 
    """
    transaction = {
        'sender': sender, 
        'recipient': recipient, 
        'amount': amount
        }
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


# function to mine a block
def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print(hashed_block)

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain), 
        'transaction': open_transactions
    }
    blockchain.append(block)

# function to get the users input of the amount of transaction
def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return tx_recipient, tx_amount

# function to receive users choices of inputs
def get_user_choice():
    return input('Your choice: ')

# Output the blockchain list to console
def print_blockchain_elements():
    for block in blockchain:
        print('_' * 20)
        print(block)
    else:
        print('_' * 20)

# a function used to validate if the blockchain is manipulated
def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True



waiting_for_input = True

while waiting_for_input:
    """ Printing out the different input options """
    print('Please choose:')
    print('1: Add a new transacion value')
    print('2: Mine a new block.')
    print('3: Output the blocks of the blockchain')
    print('4: Output participants')
    print('h: Manipulate the chain')
    print('q: Quit')
    """ receiving users choice """
    user_choice = get_user_choice()
    """ unsing conditions to invoke functions depending on users input """
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0, 
                'transaction': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 100.0}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print('Invalid blockchain!')
        break
else:
    print('User left!')
