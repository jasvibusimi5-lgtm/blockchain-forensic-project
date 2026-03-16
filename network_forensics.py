import psutil, socket
from datetime import datetime

class NetworkForensics:
    def collect(self):
        connections = []
        for conn in psutil.net_connections(kind='inet'):
            try:
                connections.append({
                    'local_address': f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A",
                    'remote_address': f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A",
                    'status': conn.status,
                    'pid': conn.pid
                })
            except:
                pass
        
        return {
            'timestamp': datetime.now().isoformat(),
            'hostname': socket.gethostname(),
            'active_connections': connections[:30],
            'interfaces': list(psutil.net_if_stats().keys())
        }