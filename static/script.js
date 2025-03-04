const socket = io();

socket.on("message", (msg) => {
    const messageContainer = document.getElementById("messages");
    const messageElement = document.createElement("div");
    messageElement.textContent = msg;
    messageContainer.appendChild(messageElement);
    messageContainer.scrollTop = messageContainer.scrollHeight;
});

function sendMessage() {
    const input = document.getElementById("message");
    const message = input.value;
    if (message.trim() !== "") {
        socket.send(message);
        input.value = "";
    }
}
