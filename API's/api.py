import random

from flask import Flask

# Flask is Class

app = Flask(__name__)  # building a flask app object using __init__()


@app.post('/hello')  # if any user sent get req to /hello resource run this function
def gett_hello():  # the return of this function will be the response of the code
    return 'world !'


@app.get('/math')
def get_math():
    x = random.randrange(1, 100)
    y = random.randrange(1, 100)
    return f'{x} + {y}  = ?'


app.run(port=8881)  # run the application
