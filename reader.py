import redis

redis_client = redis.Redis(host="redis-service", port=6379)

def process_msg():
    while True:
        message = redis_client.lpop('messages')
        if message:
            try:
                # Декодируем сообщение и разбиваем его на части
                parts = message.decode('utf-8').split()
                
                # Проверяем, что получено ровно два значения
                if len(parts) == 2:
                    timestamp, status = parts
                    print(f"Received message - Timestamp: {timestamp}, Status: {status}")
                else:
                    print(f"Unexpected message format: {message.decode('utf-8')}")

            except Exception as e:
                print(f"Error processing message: {e}")

if __name__ == "__main__":
    process_msg()
