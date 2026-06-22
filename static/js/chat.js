/* ====================================
     AI Chat Bot Support Javascript
===================================== */

document.getElementById("send-btn").addEventListener("click", function() {
    const input = document.getElementById("chat-input");
    const text = input.value.trim();
    if (!text) return;

    const chatBox = document.getElementById("chat-container");

    // User chat bubble
    const userBubble = document.createElement("div");
    userBubble.classList.add("user-bubble");
    userBubble.innerText = text;
    chatBox.appendChild(userBubble);

    input.value = "";

    // Scroll to Bottom
    chatBox.scrollTop = chatBox.scrollHeight;

    // Bot placeholder
    setTimeout(() => {
        const botBubble = document.createElement("Div");
        botBubble.classList.add("bot-bubble");
        botBubble.innerText = "Thinking......";
        chatBox.appendChild(botBubble);
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 300);
});

