import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message")
def handle_message(data):
    username = data.get("username", "Anonymous")
    message = data.get("message", "")
    print(f"Message from {username}: {message}")
    socketio.emit("message", {"username": username, "message": message})

@socketio.on("clear")
def clear_messages():
    print("Chat cleared by command.")
    socketio.emit("clear")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)