import psutil
import time
from alert import send_alert
from config import load_config
from utils import setup_logging, log_message

def check_system(config):

    cpu_usage = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    if cpu_usage > config['cpu_threshold']:
        send_alert(f"High CPU usage: {cpu_usage}%")
        log_message(f"High CPU usage detected: {cpu_usage}%", 'warning')
    if mem.available < config['mem_threshold']:
        send_alert(f"Low available memory: {mem.available} bytes")
        log_message(f"Low available memory detected: {mem.available} bytes", 'warning')
    if disk.free < config['disk_threshold']:
        send_alert(f"Low disk space: {disk.free} bytes")
        log_message(f"Low disk space detected: {disk.free} bytes", 'warning')


def main():
    config = load_config()
    while True:
        check_system(config)


if __name__ == "__main__":
    main()