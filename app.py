import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Database model for chat messages
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(200), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def handle_connect():
    # Send existing messages to the newly connected client
    messages = Message.query.all()
    for message in messages:
        socketio.emit("message", {"username": message.username, "message": message.message})

@socketio.on("message")
def handle_message(data):
    username = data.get("username", "Anonymous")
    message_text = data.get("message", "")
    message = Message(username=username, message=message_text)
    db.session.add(message)
    db.session.commit()
    print(f"Message from {username}: {message_text}")
    socketio.emit("message", {"username": username, "message": message_text})

@socketio.on("clear")
def clear_messages():
    db.session.query(Message).delete()
    db.session.commit()
    print("Chat cleared by command.")
    socketio.emit("clear")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)