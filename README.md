# Chat Application with Flask, WebSockets, and SQLite

This is a simple chat application built using Flask, Flask-SocketIO, and SQLite for local storage. The app allows users to send and receive messages in real-time, as well as clear all messages with a command.

![image](https://github.com/user-attachments/assets/b0527f06-ba07-4a46-b6bc-c328328f2d6e){: width="300px"}

## Features

- **Real-time chat**: Users can send and receive messages instantly using WebSockets.
- **Persistent storage**: All chat messages are saved in a local SQLite database, which persists even after the server restarts.
- **Clear chat**: Users can clear the entire chat history using a command.
- **Anonymous username**: If no username is provided, the system will default to "Anonymous".

# How to run Locally

### 1. Clone the Repository

`git clone https://github.com/your-username/chat-app.git  `
`cd chat-app`

### 2. Create a Virtual Environment

It is recommended to create a virtual environment to isolate the dependencies:

`python3 -m venv venv` (name as env as needed)
OR
`pyenv virtualenvs 3.9 venv` (name as env as needed)

### 3. Install Dependencies

Install the required Python packages:

`pip install -r requirements.txt`

### 4. Run the Application (Locally)

Start the Flask development server:

`python app.py`

The app will be available at `http://127.0.0.1:5000/`.

# Deployment on Render

To deploy this chat application on Render, follow these steps:

### 1. Create a Render Account

Go to [Render](https://render.com) and create an account if you don’t already have one.

### 2. Create a New Web Service on Render

- After logging in to Render, click on the **"New Web Service"** button.
- Choose the option to deploy from a **GitHub repository**.
- Select the repository where you’ve stored your chat app (either by connecting your GitHub account or pasting the repo link).
  
### 3. Set Up Render Configuration

- **Environment**: Select **Python** as the environment.
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn -k eventlet -w 1 app:app`
  
### 4. Deploy the App

Once everything is set up, click **Deploy**. Render will build and deploy your app automatically.

## Usage

- **Sending a message**: Users can send messages by typing into the input field and pressing the "Send" button. Messages are displayed in real-time for all connected clients.
- **Clearing the chat**: To clear the entire chat history, the "Clear Chat" button can be clicked, which will remove all messages from the database and notify all connected clients.

## Code Structure

- `app.py`: Main Python file for the Flask application.
- `templates/index.html`: HTML template for the frontend user interface.
- `chat.db`: SQLite database for storing messages.

## Additional Notes

- **WebSocket support**: The app uses `Flask-SocketIO` and `eventlet` to enable real-time communication via WebSockets.
- **SQLite**: A simple SQLite database is used to persist chat messages locally.


## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.
