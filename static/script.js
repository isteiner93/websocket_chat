let socket = io();
const userId = `User${Math.floor(Math.random() * 1000)}`; // Unique user ID
let username = userId; // Default username

function setUsername() {
    const input = document.getElementById("username");
    if (input.value.trim() !== "") {
        username = `${input.value} (${userId})`;
        input.value = "";
        alert(`Username set to ${username}`);
    }
}

socket.on("message", (data) => {
    const messageContainer = document.getElementById("messages");
    const messageElement = document.createElement("div");
    messageElement.textContent = `${data.username}: ${data.message}`;
    messageContainer.appendChild(messageElement);
    messageContainer.scrollTop = messageContainer.scrollHeight;
});

function sendMessage() {
    const input = document.getElementById("message");
    const message = input.value.trim();
    if (message !== "") {
        if (message === "/clearchat") {
            socket.emit("clear");
        } else {
            socket.emit("message", { username: username, message: message });
        }
        input.value = "";
    }
}

// Send message on Enter key press
document.getElementById("message").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

socket.on("clear", () => {
    const messageContainer = document.getElementById("messages");
    messageContainer.innerHTML = ""; // Clear all messages
});