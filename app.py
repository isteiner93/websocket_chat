import eventlet
eventlet.monkey_patch()  # Ensure this is called before other imports

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message")
def handle_message(msg):
    print(f"Message: {msg}")
    socketio.emit("message", msg)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)