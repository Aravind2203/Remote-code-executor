import subprocess
import os
import json


def python_executor(code):
    with open("ns.py","w") as f:
        f.write(code)
    h=subprocess.run(["python","ns.py"],capture_output=True,text=True)
    os.remove("ns.py")
    if h.stderr:
            data_={
				"error":h.stderr,
				"message":None
			}
            json_data=json.dumps(data_)
            return json_data
    else:
        data_={
			"error":None,
			"message":h.stdout
			}
        json_data=json.dumps(data_)
        return json_data

def java_executor(code):
    with open("Main.java","w") as f:
        f.write(code)
    compile_=subprocess.run(["javac","Main.java"],capture_output=True,text=True)
    if compile_.stderr:
        data_={
            "error":compile_.stderr,
            "message":None
        }
        json_data=json.dumps(data_)
        return json_data
    else:
        execute_=subprocess.run(["java","Main"],capture_output=True,text=True)
        if execute_.stderr:
            data_={
            "error":execute_.stderr,
            "message":None
            }
            json_data=json.dumps(data_)
            return json_data
        else:
            data_={
			"error":None,
			"message":execute_.stdout
			}
            json_data=json.dumps(data_)
            return json_data

def js_executor(code):
    with open("main.js","w") as f:
        f.write(code)
    h=subprocess.run(["node","main.js"],capture_output=True,text=True)
    os.remove("main.js")
    if h.stderr:
            data_={
				"error":h.stderr,
				"message":None
			}
            json_data=json.dumps(data_)
            return json_data
    else:
        data_={
			"error":None,
			"message":h.stdout
			}
        json_data=json.dumps(data_)
        return json_data
