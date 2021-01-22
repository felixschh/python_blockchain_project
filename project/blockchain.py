import functools
import hashlib as hl
from collections import OrderedDict
import json
import pickle

# import from other files
from hash_util import hash_string_256, hash_block
from block import Block


# defining our blockchain as an empty list
MINING_REWARD = 10


blockchain = []
open_transactions = []
owner = 'Max'
participants = {'Max'}


# load data from a .txt file
def load_data():
    global blockchain
    global open_transactions
    try:
        with open('blockchain.txt', mode='r') as f:
            # file_content = pickle.loads(f.read())
            file_content = f.readlines()
            # blockchain = file_content['chain']
            # open_transactions = file_content['ot']
            blockchain = json.loads(file_content[0][:-1])
            updated_blockchain = []
            for block in blockchain:
                updated_block = Block(block['index'], block['previous_hash'],
                    [OrderedDict([('sender', tx['sender']), ('recipient', tx['recipient']), 
                    ('amount', tx['amount'])]) for tx in block['transaction']],
                    block['proof'], block['timestamp'])
                updated_blockchain.append(updated_block)
            blockchain = updated_blockchain
            open_transactions = json.loads(file_content[1])
            updated_transactions = []
            for tx in open_transactions:
                updated_transaction = OrderedDict(
                    [('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])])
                updated_transactions.append(updated_transaction)
            open_transactions = updated_transactions
    except IOError:
        genesis_block = Block(0, '', [], 100, 0)

        blockchain = [genesis_block]
        open_transactions = []
        print('file not found!')
    finally:
        print('Cleanup!')
    
load_data()


# save data in .txt file
def save_data():
    try:
        with open('blockchain.txt', mode='w') as f:
            f.write(json.dumps(blockchain))
            f.write('\n')
            f.write(json.dumps(open_transactions))
            # save_data = {
            #     'chain': blockchain,
            #     'ot': open_transactions
            # }
            # f.write(pickle.dumps(save_data))
    except IOError:
        print('Saving failed!')

# function to validate hte proof of a block
def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hl.sha256(guess).hexdigest()
    print(guess_hash)
    return guess_hash[0:2] == '00'

# function to return if the proof is correct
def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof




# defining a function to get the balance of the participants
def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block.transactions if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount']for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    # amount_sent = 0
    # for tx in tx_sender:
    #     if len(tx) > 0:
    #         amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block.transactions if tx['recipient'] == participant] for block in blockchain]
    amount_received = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
    #amount_received = 0
    # for tx in tx_recipient:
    #     if len(tx) > 0:
    #         amount_received += tx[0]
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
    # transaction = {
    #     'sender': sender, 
    #     'recipient': recipient, 
    #     'amount': amount
    #     }
    transaction = OrderedDict([
        ('sender', sender), ('recipient', recipient), ('amount', amount)
        ])
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        save_data()
        return True
    return False

# function to mine a block
def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    # reward_transaction = {
    #     'sender': 'MINING',
    #     'recipient': owner,
    #     'amount': MINING_REWARD
    # }
    reward_transaction = OrderedDict(
        [('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REWARD)])
    copied_transactions = open_transactions[:] 
    copied_transactions.append(reward_transaction)
    block = Block(len(blockchain), hashed_block, copied_transactions, proof)
    blockchain.append(block)
    save_data()
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
        if block.previous_hash != hash_block(blockchain[index - 1]):
            return False
        if not valid_proof(block['transaction'][:-1], block.previous_hash, block['proof']):
            print('Proof of work is invalid!')
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
            save_data()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print('Invalid blockchain!')
        break
    print('Balance of {}: {:6.2f}'.format(owner, get_balance(owner)))
else:
    print('User left!')
