let socket = io();
let username = `User${Math.floor(Math.random() * 1000)}`; // Default username

function setUsername() {
    const input = document.getElementById("username");
    if (input.value.trim() !== "") {
        username = input.value;
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
    const message = input.value;
    if (message.trim() !== "") {
        socket.emit("message", { username: username, message: message });
        input.value = "";
    }
}