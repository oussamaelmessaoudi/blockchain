import hashlib

class Block:
    def __init__(self,index,timestamp,data,previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()[:5]


genesis_block = Block(0, "2025-10-12    00:00","Bloc de genèse",previous_hash="0")
blockchain =  [genesis_block]

print("Index : ",genesis_block.index)
print("Timestamp : ",genesis_block.timestamp)
print("Données : ",genesis_block.data)
print("Previous Hash : ",genesis_block.previous_hash)
print("Hash : ",genesis_block.hash)

# Créer un second bloc
bloc1 = Block(1, "2025-10-12    00:05","Alice envoie 5 BTC", previous_hash=genesis_block.hash)
blockchain.append(bloc1)
for bloc in blockchain:
    print(f"Bloc          {bloc.index}      :       data = {bloc.data}, prev_has= {bloc.previous_hash}, hash= {bloc.hash}")