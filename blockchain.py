# defining our blockchain as an empty list
blockchain = [[1]]


def add_value():
    blockchain.append([blockchain[-1], 5.3])
    print(blockchain)


add_value()
add_value()
add_value()
