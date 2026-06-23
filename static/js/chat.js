/* ====================================
     AI Chat Bot Support Javascript
===================================== */

document.getElementById("send-btn").addEventListener("click", async function() {
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
    const botBubble = document.createElement("Div");
    botBubble.classList.add("bot-bubble");
    botBubble.innerText = "Thinking......";
    chatBox.appendChild(botBubble);
    chatBox.scrollTop = chatBox.scrollHeight;

    const response = await fetch("/send_message", {
        method:"POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text })
    });

    const data = await response.json();

    botBubble.innerText = data.ai;
});

