from web3 import Web3
import json, os, hashlib
from config import Config

class BlockchainHandler:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(Config.BLOCKCHAIN_URL))
        if not self.w3.is_connected():
            raise Exception("Cannot connect to blockchain!")
        
        # Load ABI
        with open('contracts/contract_abi.json', 'r') as f:
            abi = json.load(f)
        
        self.contract = self.w3.eth.contract(
            address=Config.CONTRACT_ADDRESS,
            abi=abi
        )
        self.account = Config.ACCOUNT_ADDRESS
        self.private_key = Config.PRIVATE_KEY
        print("[+] Blockchain connected!")
    
    @staticmethod
    def generate_evidence_id(session_id):
        return f"EVD-{session_id}"
    
    def register_evidence(self, evidence_id, evidence_hash, os_source, forensic_type, tools_used):
        try:
            txn = self.contract.functions.registerEvidence(
                evidence_id, evidence_hash, os_source, forensic_type, tools_used
            ).build_transaction({
                'from': self.account,
                'nonce': self.w3.eth.get_transaction_count(self.account),
                'gas': 500000,
                'gasPrice': self.w3.to_wei('20', 'gwei')
            })
            
            signed = self.w3.eth.account.sign_transaction(
                txn, 
                self.private_key
            )
            
            # ✅ Fixed line - using raw_transaction instead of rawTransaction
            tx_hash = self.w3.eth.send_raw_transaction(
                signed.raw_transaction
            )
            
            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            
            return {
                'status': 'success',
                'transaction_hash': tx_hash.hex(),
                'block_number': receipt['blockNumber']
            }
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
    
    def verify_evidence_hash(self, evidence_id, hash_to_verify):
        return self.contract.functions.verifyHash(
            evidence_id, 
            hash_to_verify
        ).call()
    
    def get_account_balance(self):
        balance_wei = self.w3.eth.get_balance(self.account)
        return self.w3.from_wei(balance_wei, 'ether')