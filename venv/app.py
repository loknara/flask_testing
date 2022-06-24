from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/loke')
def lok():
    return "hello loke"

if __name__ == '__main__':
    app.run(debug=True)