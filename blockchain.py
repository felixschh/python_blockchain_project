# defining our blockchain as an empty list
MINING_REWARD = 10


genesis_block = {
    'previous_hash': '',
    'index': 0, 
    'transaction': []}
blockchain = [genesis_block]
open_transactions = []
owner = 'Max'
participants = {'Max'}

# defining function to create a hashed block
def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

# defining a function to get the balance of the participants
def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transaction'] if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount']for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transaction'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent


# defining function that returns last blockchain value
def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


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
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False

# function to mine a block
def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:] 
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain), 
        'transaction': copied_transactions
    }
    blockchain.append(block)
    return True

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


# def verify_transactions():
#     is_valid = True
#     for tx in open_transactions:
#         if verify_transaction(tx):
#             is_valid = True
#         else: 
#             is_valid = False
#         return is_valid


waiting_for_input = True

while waiting_for_input:
    """ Printing out the different input options """
    print('Please choose:')
    print('1: Add a new transacion value')
    print('2: Mine a new block.')
    print('3: Output the blocks of the blockchain')
    print('4: Output participants')
    # print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q: Quit')
    """ receiving users choice """
    user_choice = get_user_choice()
    """ using conditions to invoke functions depending on users input """
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('Added transaction!')
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    # elif user_choice == '5':
    #     if verify_transactions():
    #         print('All transactions are valid')
    #     else:
    #         print('There are invalid transactions')
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
    print('Balance of {}: {:6.2f}'.format('Max', get_balance('Max')))
else:
    print('User left!')
