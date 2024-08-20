from flask import Flask, request

app = Flask(__name__)

@app.before_request
def remove_server_header():
    if 'Server' in request.headers:
        del request.headers['Server']

@app.route('/')
def home():
    return "Welcome to the secure OpenEMR application!"

if __name__ == '__main__':
    app.run()
