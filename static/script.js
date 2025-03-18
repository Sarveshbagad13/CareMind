function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    var chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class="user-message">${userInput}</div>`;

    fetch(`/get?msg=${userInput}`)
        .then(response => response.text())
        .then(botResponse => {
            chatBox.innerHTML += `<div class="bot-message">${botResponse}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        });

    document.getElementById("user-input").value = "";
}

function handleKeyPress(event) {
    if (event.keyCode === 13) {
        sendMessage();
    }
}
