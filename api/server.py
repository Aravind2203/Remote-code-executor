from fastapi import FastAPI
from models import *
from config import *
import json

app=FastAPI()


@app.post("/execute")
def execute(request:Code):
    data={
        "code":request.code
    }
    json_data=json.dumps(data)
    rabitcon=RabitMQConnection(json_data)
    return {
        "message":"Task Scheduled"
    }

@app.get("/result")
def get_result():
    r=RedisConnection()
    response=r.get_key("hello")
    json_response=json.loads(response)
    return json_response