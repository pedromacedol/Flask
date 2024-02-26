from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

@app.route('/<name>')
def print_name(name):
    return 'hello, {}'.format(name)

if __name__ == "__main__":
    app.run()