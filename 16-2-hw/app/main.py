from flask import Flask, request
import requests
import time


app = Flask(__name__)

pc_list = [
    {'brand': 'hp', 'cpu': 16, 'color': 'red'},
    {'brand': 'lenovo', 'cpu': 16, 'color': 'yellow'}
]


@app.get('/')
def main_page():
    return "hello", 200


@app.get('/pc')
def get_all():
    return pc_list


@app.get('/pc/<int:id>')
def get_by_id(id):
    return pc_list[id-1]


@app.post('/pc')
def add_pc():
    new_data = request.json
    pc_list.append(new_data)
    keys = list(pc_list[0].keys())
    for key in keys:
        if key not in new_data.keys():
            return f'missing {key}', 400
    pc_list.append(new_data)
    return {'Status': 'Done', 'Message': 'new pc added'}


@app.put('/pc/<int:id>')
def update_pc(id):
    new_data = request.json
    pc_list.pop(id-1)
    return {'Status': 'Done', 'message': 'get replaced'}


@app.delete('/pc/<int:id>')
def delete_pc(id):
    new_data = request.json
    pc_list.pop(id-1)
    return {'Status': 'Done', 'message': 'pc deleted'}


@app.get('/test')
def is_healthy():
    return '200', 200


@app.get('/healthy')
def is_ready():
    time.sleep(10)
    res = requests.get('https://www.google.com')
    if res.status_code < 400:
        return "200", 200
    return '400', 400

# @app.after_request()
# def after():
#     return ""

# @app.before_request()
# def before():
#     return

app.run(port=5000, host='0.0.0.0')
