from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hi')
def hello_world():
    return 'Hello World!'

@app.route("/")
@app.route("/<name>")
def index(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()
