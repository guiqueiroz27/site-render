from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Opa, <b>tudo bem</b>?"

@app.route("/teste")
def teste():
  return "Essa página é um <b>teste</b> lb=brbr"