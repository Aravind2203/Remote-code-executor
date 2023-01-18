import pika
import redis

class RabitMQConnection:
    def __init__(self,code):
        self.connection=pika.BlockingConnection(pika.URLParameters("amqp://admin:pass@rabbitmq:5672"))
        self.channel=self.connection.channel()
        self.channel.queue_declare(queue="hello")
        self.channel.basic_publish(exchange="",routing_key="hello",body=code)
        print("[X]Task successfully scheduled")
        self.connection.close()

class RedisConnection:
    def __init__(self):
        self.conn=redis.Redis(host='redis-server',port=6379)
    
    def set_key(self,key,msg):
        self.conn.set(key,msg)
    
    def get_key(self,key):
        return self.conn.get(key)