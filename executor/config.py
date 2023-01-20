import pika
import redis
import subprocess
import json
import os
from lang import *
class RedisConnection:
    def __init__(self):
        self.conn=redis.Redis(host='redis-server',port=6379)
    
    def set_key(self,key,msg):
        self.conn.set(key,msg)
    
    def get_key(self,key):
        return self.conn.get(key)

class RabitMQConnection:
    def __init__(self):
        self.connection=pika.BlockingConnection(pika.URLParameters("amqp://admin:pass@rabbitmq:5672"))
        self.channel=self.connection.channel()
        self.channel.queue_declare(queue="hello")
        self.r=RedisConnection()
    
    def callbacks(self,ch,method,properties,body):
        body=body.decode()
        data=json.loads(body)
        if data["lang"]=="python":
            response=python_executor(data["code"])
        if data["lang"]=="java":
            response=java_executor(data["code"])
        if data["lang"]=="node":
            response=js_executor(data["code"])
        self.r.set_key(data["task_id"],response)
        
    def consume_task(self):
        self.channel.basic_consume(queue="hello",on_message_callback=self.callbacks,auto_ack=True)
        self.channel.start_consuming()

