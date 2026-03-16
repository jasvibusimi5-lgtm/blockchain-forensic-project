import psutil
from datetime import datetime

class MemoryForensics:
    def collect(self):
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'memory_info', 'status']):
            try:
                processes.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'memory_mb': round(proc.info['memory_info'].rss / 1024 / 1024, 2),
                    'status': proc.info['status']
                })
            except:
                pass
        
        return {
            'timestamp': datetime.now().isoformat(),
            'total_ram_gb': round(psutil.virtual_memory().total / 1e9, 2),
            'used_ram_percent': psutil.virtual_memory().percent,
            'processes': processes[:50]
        }