"""
    一个区块:
    {
        "index":0,                      #索引
        "timestamp":"",                 #时间戳
        "transactions":[                #交易信息集合
            {
                "sender":"",            #交易发送者
                "recipient":"",         #交易接收者
                "amount":5,             #交易金额
            }
        ],
        "proof":"",                     #工作量证明
        "previous_hash":""              #上一个区块的哈希值
    }
"""
from time import time
import hashlib
import json
import requests
from uuid import uuid4
from urllib.parse import urlparse

from flask import Flask, jsonify, request


class Blockchain:
    def __init__(self):
        self.chain=[]                   #区块链
        self.current_transactions=[]    #交易信息集合
        self.nodes=set()                #保存节点信息

        self.new_block(proof=100,previous_hash=1)   #第一个区块(创世纪区块)

    def register_node(self,address):
        '''注册一个节点'''
        parsed_url=urlparse(address)
        self.nodes.add(parsed_url.netloc)       #去掉http://

    def new_block(self,proof,previous_hash=None):
        '''添加一个新块'''
        block={
            "index":len(self.chain)+1,
            "timestamp":time(),
            "transactions":self.current_transactions,
            "proof":proof,
            "previous_hash":previous_hash or self.hash(self.last_block)
        }

        self.current_transactions=[]        #清空交易信息
        self.chain.append(block)
        return block

    def new_transactions(self,sender,recipient,amount):
        '''添加一笔新的交易'''
        self.current_transactions.append(
            {
                "sender": sender,
                "recipient": recipient,
                "amount": amount
            }
        )
        return self.last_block['index']+1       #返回添加到哪个区块的序号

    def resolve_conflicts(self):
        '''解决冲突'''
        neighbours=self.nodes                   #获取所有节点
        max_length=len(self.chain)              #先默认最长的链是自己
        new_chain=None                          #最终链

        for node in neighbours:
            response=requests.get(f'http://{node}/chain')   #获取每个节点现在的区块链
            if response.status_code==200:
                length=response.json()['length']
                chain=response.json()['chain']

                if length>max_length and self.valid_chain(chain):
                    max_length=length
                    new_chain=chain
        if new_chain:
            self.chain=new_chain                #覆盖最终链
            return True                         #返回True代表被取代
        return False

    def valid_chain(self,chain):
        '''验证区块链的有效性'''
        last_block=chain[0]
        current_index=1

        while current_index<len(chain):         #从整个链的第一个块开始遍历
            block=chain[current_index]
            if block['previous_hash']!=self.hash(last_block):   #验证上个块的hash值
                return False
            if not self.valid_proof(last_block['proof'],block['proof']):    #验证工作量是不是以0000开头
                return False

            last_block=block
            current_index+=1
        return True

    @staticmethod
    def hash(block):
        '''计算区块的哈希值'''
        block_string=json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        '''获取区块链里的最后一个块'''
        return self.chain[-1]

    def proof_of_work(self,last_proof):
        '''工作量证明'''
        proof=0
        while self.valid_proof(last_proof,proof) is False:
            proof+=1
        print("工作量：",proof)
        return proof            #返回工作量(随机数)

    def valid_proof(self,last_proof,proof):
        '''验证工作量正确性'''
        guess=f'{last_proof}{proof}'.encode()
        guess_hash=hashlib.sha256(guess).hexdigest()

        return guess_hash[0:4]=="0000"

'''==============================================='''
app=Flask(__name__)

blockchain=Blockchain()
node_identifier=str(uuid4()).replace('-','')    #自己的地址

@app.route('/',methods=['GET'])
def index():
    return "Welcome"

@app.route('/transactions/new',methods=['POST'])
def new_transaction():
    '''添加新交易'''
    values=request.get_json()
    required=["sender","recipient","amount"]

    if values is None:
        return "Missing values",400
    if not all(k in values for k in required):
        return "Missing values",400

    index=blockchain.new_transactions(values['sender'],values['recipient'],values['amount'])
    response={"message":f'Transcation will be added to Block: {index}'}
    return jsonify(response),201

@app.route('/mine',methods=['GET'])
def mine():
    '''打包交易(挖矿)'''
    last_block=blockchain.last_block
    last_proof=last_block['proof']
    proof=blockchain.proof_of_work(last_proof)      #新的工作量

    blockchain.new_transactions(sender="0",         #添加一笔给自己的转账
                                recipient=node_identifier,amount=1)
    block=blockchain.new_block(proof,None)          #用新的工作量建立一个新区块
    response={
        "message":"New Block Created",
        "index":block['index'],
        "transactions":block['transactions'],
        "proof":block['proof'],
        "previous_hash":block['previous_hash']
    }
    return jsonify(response)


@app.route('/chain',methods=['GET'])
def full_chain():
    '''返回整个区块链'''
    response={
        'chain':blockchain.chain,
        'length':len(blockchain.chain)
    }
    return jsonify(response),200

@app.route('/nodes/register',methods=['POST'])
def register_nodes():
    '''注册节点'''
    values=request.get_json()
    nodes=values.get("nodes")
    if nodes is None:
        return "Error: please supply a valid list of nodes",400
    for node in nodes:
        blockchain.register_node(node)

    response={
        "message":"New nodes have been added",
        "total_nodes":list(blockchain.nodes)
    }
    return jsonify(response),201

@app.route('/nodes/resolve',methods=['GET'])
def consensus():
    '''验证自己的区块链是否被取代'''
    replaced=blockchain.resolve_conflicts()
    if replaced:
        response={
            'message':'Our chain was replaced',
            'new_chain':blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }
    return jsonify(response)

if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=5000,debug=False)
    app.run(host='0.0.0.0',port=5001,debug=False)

























