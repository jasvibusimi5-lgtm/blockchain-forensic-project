import os, platform
from datetime import datetime

class LogForensics:
    def collect(self):
        logs = []
        
        if platform.system() == 'Linux':
            log_files = ['/var/log/syslog', '/var/log/auth.log']
        elif platform.system() == 'Darwin':
            log_files = ['/var/log/system.log']
        else:
            log_files = []  # Windows needs different approach
        
        for logfile in log_files:
            if os.path.exists(logfile):
                try:
                    with open(logfile, 'r', errors='ignore') as f:
                        lines = f.readlines()[-50:]  # last 50 lines
                        logs.append({'file': logfile, 'lines': lines})
                except:
                    pass
        
        return {
            'timestamp': datetime.now().isoformat(),
            'platform': platform.system(),
            'logs_collected': logs
        }