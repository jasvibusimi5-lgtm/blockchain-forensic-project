import json
from datetime import datetime

class EvidenceLogger:
    def __init__(self, session_dir):
        self.session_dir = session_dir
        self.log_file = f"{session_dir}/evidence_log.json"
        self.logs = []
    
    def log_event(self, event_type, details):
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'event_type': event_type,
            'details': details
        }
        self.logs.append(log_entry)
        self._save_logs()
    
    def _save_logs(self):
        with open(self.log_file, 'w') as f:
            json.dump(self.logs, f, indent=2)
    
    def get_logs(self):
        return self.logs