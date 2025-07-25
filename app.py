from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Subdomain Takeover</title>
  <style>
    body {
      margin: 0;
      height: 100vh;
      background: linear-gradient(to bottom right, #000000, #003300);
      color: #00FF00;
      font-family: 'Courier New', Courier, monospace;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
    }
    h1 {
      font-size: 3em;
      text-shadow: 0 0 5px #00FF00;
    }
    p, a {
      font-size: 1.2em;
      color: #00FF00;
      text-decoration: underline;
    }
    .box {
      border: 1px solid #00FF00;
      padding: 2rem;
      border-radius: 10px;
      background: rgba(0, 0, 0, 0.6);
      box-shadow: 0 0 10px #00FF00;
    }
  </style>
</head>
<body>
  <div class="box">
    <h1>Subdomain Takeover by Asif</h1>
    <p>
      <a href="https://www.asifnawazminhas.com/" target="_blank">asifnawazminhas.com</a> &nbsp; | &nbsp;
      <a href="https://www.linkedin.com/in/asifminhasnl/" target="_blank">LinkedIn</a>
    </p>
  </div>
</body>
</html>
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
