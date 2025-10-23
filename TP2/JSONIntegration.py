from BlockHashing import Block
import json

blockchain = []
blockchain.append(Block(0, '2024-01-01 00:00:00', 'Genesis Block', previous_hash='0'))
blockchain.append(Block(1, '2024-01-01 01:00:00', 'Alice sent 5 BTC to Bob', previous_hash=blockchain[0].hash))
blockchain.append(Block(2, '2024-01-01 02:00:00', 'Bob sent 2 BTC to Charlie', previous_hash=blockchain[1].hash))

# Saving blockchain to JSON file
with open('TP2/blockchain_transactions.json', 'w') as f:
    json_blockchain = [{
        'index': block.index,
        'timestamp': block.timestamp,
        'data': block.data,
        'previous_hash': block.previous_hash,
        'hash': block.hash
        } for block in blockchain
    ]
    json.dump(json_blockchain, f, indent=4)
