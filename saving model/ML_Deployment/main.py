

# importing the lib
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/images')
def images():
    return "this is the image page"


# contact
@app.route('/contact')
def contact():
    return "this is the contact page"


# aboutus
@app.route('/aboutus')
def aboutus():
    return "this is the aboutus page"


app.run() # should be always at the end


"""
http: hyper text transfer protocol
127.0.0.1 - ip address - localhost
:5000 - port
/ - route

http://127.0.0.1:5000/

"""
