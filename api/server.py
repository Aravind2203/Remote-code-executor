from fastapi import FastAPI
from models import *
from config import *
import json
import uuid

app=FastAPI()


@app.post("/execute")
def execute(request:Code):
    id_=str(uuid.uuid1())[0:8]
    data={
        "code":request.code,
        "lang":request.lang,
        "task_id":id_
    }
    json_data=json.dumps(data)
    rabitcon=RabitMQConnection(json_data)
    return {
        "message":"Task Scheduled",
        "task_id":id_
    }

@app.get("/result/{task_id}")
def get_result(task_id:str):
    r=RedisConnection()
    response=r.get_key(task_id)
    json_response=json.loads(response)
    return json_response