from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return '''
    Hello, World!<br><br>
    Subdomain takeover by 
    <a href="https://www.asifnawazminhas.com/" target="_blank">asifnawazminhas.com</a> and 
    <a href="https://www.linkedin.com/in/asifminhasnl/" target="_blank">LinkedIn</a>
    '''
