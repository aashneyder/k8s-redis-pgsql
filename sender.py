import redis
import random
from datetime import datetime
import time

redis_client = redis.Redis(host="redis-service", port=6379)

stats = ['success', 'failed', 'paused']

def send_msg():
    timestamp = datetime.now().isoformat()
    status = random.choice(stats)

    msg = f"{timestamp} {status}"
    redis_client.rpush('messages', msg)
    print(f"Message sent {msg}")

if __name__ == "__main__":
    while True:
        send_msg()
        time.sleep(random.randint(5, 30)) 

