
from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
sio = SocketIO(
    app,
    cors_allowed_origins=['*'],
)

def main():
    app.add_url_rule(
        '/',
        view_func=lambda:render_template('index.html'))
    sio.run(
        app=app,
        host='localhost',
        port='8080',
        
    )
    return

if __name__=="__main__":
    main()