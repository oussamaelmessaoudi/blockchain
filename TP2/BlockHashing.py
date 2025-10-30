import hashlib

class Block:
    def __init__(self,index,timestamp, data, previous_hash=''):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def remove_block(self, blockchain, index):
        if 0 <= index >= len(blockchain):
            raise IndexError("Can't remove block from the blockchain.")
        del blockchain[index]
        # We will have to change the previous_hash, nonce, and chain of subsequent blocks
        for i in range(index, len(blockchain)):
            blockchain[i].previous_hash = blockchain[i-1].hash if i > 0 else '0'
            blockchain[i].nonce = 0
            blockchain[i].hash = blockchain[i].calculate_hash()
        
        return blockchain
        
# Example usage:

genesis_block = Block(0, '2024-01-01 00:00:00', 'Genesis Block', previous_hash='0')
blockchain = [genesis_block]
print(f"Block 0 Hash: {genesis_block.hash}")
# Modifying the data to see hash change
genesis_block.data = 'Modified Genesis Block'
print(f"Modified Block 0 Hash: {genesis_block.calculate_hash()}")

# Creating a 2nd block
second_block = Block(1, '2024-01-01 01:00:00', 'Second Block', previous_hash=genesis_block.hash)
blockchain.append(second_block)
print(f"Block 1 Hash: {second_block.hash}")
third_block = Block(2, '2024-01-01 02:00:00', 'Third Block', previous_hash=second_block.hash)
print(f"Block 2 Hash before mining: {third_block.hash}")

# Attempting to remove a block
try:
    blockchain = third_block.remove_block(blockchain, 4)
except IndexError as e:
    print(e)

# Display the blockchain
for block in blockchain:
    print(f"Block {block.index}: data = {block.data}, prev_hash = {block.previous_hash}, hash = {block.hash}")
