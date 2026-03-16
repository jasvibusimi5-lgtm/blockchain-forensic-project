import os, platform
from datetime import datetime

class DiskForensics:
    def collect(self):
        result = {
            'timestamp': datetime.now().isoformat(),
            'platform': platform.system(),
            'disk_info': [],
            'recent_files': []
        }
        
        # List files in home directory
        home = os.path.expanduser("~")
        for item in os.listdir(home)[:20]:  # limit to 20
            full_path = os.path.join(home, item)
            stat = os.stat(full_path)
            result['disk_info'].append({
                'name': item,
                'size': stat.st_size,
                'modified': datetime.fromtimestamp(stat.st_mtime).isoformat()
            })
        
        return result