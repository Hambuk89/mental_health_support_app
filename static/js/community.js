/* ====================================
     Community Channel Javascript
===================================== */

if (document.getElementById("category-selection")) {

    const messages = {
        "Life / Workplace Stress": [],
        "Mind & Body Symptoms": [],
        "Motivation": [],
        "Casual Lounge": [],
    };

    let currentCategory = null;

    function scrollToBottom() {
        const chatArea = document.getElementById("chat-area");
        chatArea.scrollTop = chatArea.scrollHeight;
    }

    function openBoard(category) {
        document.getElementById('category-selection').style.display = 'none';
        document.getElementById('board-section').style.display = 'block';
        document.getElementById('board-title').innerText = category;

        const chatArea = document.getElementById('chat-area');
        chatArea.innerHTML = "";

        messages[category].forEach(msg => {
            const msgDiv = document.createElement('div');
            msgDiv.classList.add('message', 'user-message');
            msgDiv.innerText = msg;
            chatArea.appendChild(msgDiv);
        });

        scrollToBottom();
    }

    function backToCategory() {
        document.getElementById('board-section').style.display = 'none';
        document.getElementById('category-selection').style.display = 'block';
    }

    function submitMessage() {
        const message = document.getElementById('message-input').value.trim();
        if (!message) return;

        const chatArea = document.getElementById('chat-area');
        const msgDiv = document.createElement('div');
        msgDiv.classList.add('message', 'user-message');
        msgDiv.innerText = message;

        chatArea.appendChild(msgDiv);

        messages[currentCategory].push(message);

        document.getElementById('message-input').value = '';

        scrollToBottom();
    }
}