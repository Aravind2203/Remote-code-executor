import pika
import redis
import subprocess
import json
import os
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
        with open("ns.py","w") as f:
            f.write(data["code"])

        h=subprocess.run(["python","ns.py"],capture_output=True,text=True)
        os.remove("ns.py")
        if h.stderr:
            data={
				"error":h.stderr,
				"message":None
			}
            json_data=json.dumps(data)
            self.r.set_key("hello",json_data)
        else:
            data={
			"error":None,
			"message":h.stdout
			}
            json_data=json.dumps(data)
            self.r.set_key("hello",json_data)
    def consume_task(self):
        self.channel.basic_consume(queue="hello",on_message_callback=self.callbacks,auto_ack=True)
        self.channel.start_consuming()

