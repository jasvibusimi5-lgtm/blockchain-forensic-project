import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class Config:
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'changeme')
    
    INVESTIGATOR_ID = os.getenv('INVESTIGATOR_ID', 'INV-001')
    ORGANIZATION = os.getenv('ORGANIZATION', 'CyberLab')
    
    BLOCKCHAIN_URL = os.getenv('BLOCKCHAIN_URL', 'http://127.0.0.1:7545')
    CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS', '')
    PRIVATE_KEY = os.getenv('PRIVATE_KEY', '')
    ACCOUNT_ADDRESS = os.getenv('ACCOUNT_ADDRESS', '')
    
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    GROQ_API_KEY = os.getenv('GROQ_API_KEY', '')
    
    BASE_EVIDENCE_DIR = 'evidence_output'
    
    @staticmethod
    def create_session_directory():
        session_id = datetime.now().strftime('%Y%m%d_%H%M%S')
        session_dir = os.path.join(Config.BASE_EVIDENCE_DIR, session_id)
        os.makedirs(session_dir, exist_ok=True)
        return session_dir, session_id
    
    @staticmethod
    def validate_config():
        errors = []
        if not Config.CONTRACT_ADDRESS:
            errors.append("CONTRACT_ADDRESS not set")
        if not Config.PRIVATE_KEY:
            errors.append("PRIVATE_KEY not set")
        if not Config.OPENAI_API_KEY:
            errors.append("OPENAI_API_KEY not set")
        return errors


