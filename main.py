# SAMPLE CRYPTOCURRENCY USING BLOCKCHAIN
# referenced from https://github.com/Savjee/SavjeeCoin and https://github.com/droid76/Merkle-Tree

import hashlib
import datetime
from datetime import datetime
    
class MerkleTreeNode:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        self.hashValue = hashlib.sha256(value.encode('utf-8')).hexdigest()
    
def buildTree(leaves):
    nodes = []
    for i in leaves:
        nodes.append(MerkleTreeNode(i))
        
    while len(nodes)!=1:
        temp = []
        for i in range(0,len(nodes),2):
            node1 = nodes[i]
            if i+1 < len(nodes):
                node2 = nodes[i+1]
            else:
                temp.append(nodes[i])
                break
            # print("Left child : "+ node1.value + " | Hash : " + node1.hashValue +" \n")
            # print("Right child : "+ node2.value + " | Hash : " + node2.hashValue +" \n")
            concatenatedHash = node1.hashValue + node2.hashValue
            parent = MerkleTreeNode(concatenatedHash)
            parent.left = node1
            parent.right = node2
            # print("Parent(concatenation of "+ node1.value + " and " + node2.value + ") : " +parent.value + " | Hash : " + parent.hashValue +" \n")
            temp.append(parent)
        nodes = temp 
    return nodes[0]

# inputString = str(input())
# leavesString = inputString[1:len(inputString)-1]
# leaves = leavesString.split(",")
# root = buildTree(leaves)
# print(root.hashValue)

class Transaction:
    def __init__(self,fromaddress,toaddress,amount):
        self.fromad = fromaddress
        self.toad = toaddress
        self.amt = amount
        

class Block:
    def __init__(self,timestamp,transaction,previousHash=''):
        self.nonce = 0
        self.timestamp = timestamp
        self.transaction = transaction
        self.merkinp = ''
        for i in transaction:
            self.merkinp = self.merkinp+i.fromad+','+i.toad+','+i.amt+','

        self.roothash = buildTree(self.merkinp.split(",")).hashValue
        self.previousHash = previousHash
        self.hash = self.calculateHash()
        

    def calculateHash(self):
        res = self.roothash+str(self.nonce)+str(self.timestamp)
        res = hashlib.sha256(res.encode())
        return res.hexdigest()

    def mineBlock(self,difficulty):
        a = ''
        for i in range(difficulty):
            a=a+'0'
        while self.hash[0:difficulty] != a:
                # print(self.hash[0:difficulty+1])
                self.nonce+=1
                self.hash = self.calculateHash()
        print("Block Mined: ", self.hash)

class Blockchain:
    def __init__(self):
        self.difficulty = 3
        self.pendingTransactions = []
        self.miningReward = "100"
        self.chain = [self.createGenesisBlock()]
        

    def createGenesisBlock(self):
        ret = Block(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),[Transaction("sender","reciever","0")], "0")
        print("Genesis Block being created...please hold on")
        print("----------------------------------------------------")
        ret.mineBlock(self.difficulty)
        print("Block successfully mined!")
        self.pendingTransactions.append(Transaction("null","0",self.miningReward))
        print("----------------------------------------------------")
        return ret

    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]

    # def addBlock(self,v):
    #     v.previousHash = self.getLatestBlock().hash
    #     v.mineBlock(self.difficulty)
    #     self.chain.append(v)

    def minePendingTransactions(self,mineradd,timestamp=datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        print("----------------------------------------------------")
        if(len(self.pendingTransactions)>3):
            send=self.pendingTransactions[0:3]
            self.pendingTransactions=self.pendingTransactions[3:]
        else:
            send = self.pendingTransactions
            self.pendingTransactions=[]
        v = Block(timestamp, send, self.getLatestBlock().hash)
        v.mineBlock(self.difficulty)
        print("Block successfully mined!")
        self.chain.append(v)
        self.pendingTransactions.append(Transaction("null",mineradd,self.miningReward))
        print("----------------------------------------------------")

    def isChainValid(self):
        for i in range(1, len(self.chain)):
            if( self.chain[i].hash != self.chain[i].calculateHash()):
                return False 
            if( self.chain[i].previousHash != self.chain[i-1].hash):
                return False
        return True


def main():
    print("SAMPLE CRYPTOCURRENCY USING BLOCKCHAIN:")
    print("referenced from https://github.com/Savjee/SavjeeCoin and https://github.com/droid76/Merkle-Tree")
    print("------------------------------------------------------------------------------------------------")
    c=1
    t=1
    ccoin = Blockchain()
    while c==1:
        sadd=""
        radd=""
        amt=""
        print("TRANSACTION #",t)
        print("ENTER SENDER'S ADDRESS:")
        sadd = str(input())
        print("ENTER RECIEVER'S ADDRESS:")
        radd = str(input())
        print("ENTER AMOUNT:")
        amt = str(input())
        ccoin.pendingTransactions.append(Transaction(sadd,radd,amt))
        print("EXIT - enter 0")
        print("MORE TRANSACTION - enter 1")
        c = int(input())
        t+=1
    print("Your transactions are being added to the blockchain...please wait")
    while len(ccoin.pendingTransactions)>1:
        ccoin.minePendingTransactions("miner01")
    # ccoin.addBlock( Block("01/02/2020", "amount: 4") )
    # ccoin.addBlock( Block("01/03/2020", "amount: 16") )
    i=0
    for x in ccoin.chain:
        print("Block #",i,": ")
        print("Timestamp:", x.timestamp)
        print("Transactions stored in block",i,":",x.merkinp)
        print("Hash: ",x.hash)
        print("previous hash:", x.previousHash)
        i=i+1
    # to tamper with the chain, uncomment below line of code.
    # ccoin.chain[1].transaction="amount: 10" 
    print("----------------------------------------------------")
    print("coin validity:")
    print(ccoin.isChainValid())
    print("Transactions recorded!")
    print("----------------------------------------------------")

if __name__ == '__main__':
    main()
