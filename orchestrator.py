import json, hashlib, os
from datetime import datetime
from .disk_forensics import DiskForensics
from .memory_forensics import MemoryForensics
from .network_forensics import NetworkForensics
from .log_forensics import LogForensics

class ForensicOrchestrator:
    def __init__(self, session_dir, session_id):
        self.session_dir = session_dir
        self.session_id = session_id
        self.evidence_data = {
            'session_id': session_id,
            'timestamp': datetime.now().isoformat(),
            'forensics': {}
        }
    
    @staticmethod
    def list_available_tools():
        return ['disk_forensics', 'memory_forensics', 'network_forensics', 'log_forensics']
    
    def execute_forensics(self, forensic_types):
        if 'all' in forensic_types or 'memory' in forensic_types:
            print("[*] Running memory forensics...")
            self.evidence_data['forensics']['memory'] = MemoryForensics().collect()
        
        if 'all' in forensic_types or 'network' in forensic_types:
            print("[*] Running network forensics...")
            self.evidence_data['forensics']['network'] = NetworkForensics().collect()
        
        if 'all' in forensic_types or 'disk' in forensic_types:
            print("[*] Running disk forensics...")
            self.evidence_data['forensics']['disk'] = DiskForensics().collect()
        
        if 'all' in forensic_types or 'log' in forensic_types:
            print("[*] Running log forensics...")
            self.evidence_data['forensics']['log'] = LogForensics().collect()
        
        return self.evidence_data
    
    def save_master_json(self):
        path = os.path.join(self.session_dir, 'master_evidence.json')
        with open(path, 'w') as f:
            json.dump(self.evidence_data, f, indent=2, default=str)
        print(f"[+] Master JSON saved: {path}")
    
    def calculate_evidence_hash(self):
        data_str = json.dumps(self.evidence_data, sort_keys=True, default=str)
        return hashlib.sha256(data_str.encode()).hexdigest()
    
    def get_evidence_summary(self):
        return {
            'session_id': self.session_id,
            'evidence_hash': self.calculate_evidence_hash(),
            'os_source': 'Linux/Windows/Mac',
            'forensic_types': list(self.evidence_data['forensics'].keys()),
            'tools_used': ForensicOrchestrator.list_available_tools()
        }