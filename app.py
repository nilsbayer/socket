from flask import Flask, render_template, request, flash, url_for, redirect, jsonify, abort, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__, static_url_path="/")

app.config['SECRET_KEY'] = "test123"
socketio = SocketIO(app)

# DB_PWD = os.getenv("DB_PWD")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('connection')  # Event handler for 'message' event
def handle_message():
    session_id = request.sid
    print(f"Message received from client. Session ID: {session_id}")
    room = "play"
    join_room(room)
    emit("server-message", "New Player joined the room", to=room)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")