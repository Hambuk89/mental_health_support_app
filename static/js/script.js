/* ==================================
          Q&A Forum Javascript
================================== */
const questionList = document.getElementById("questionList");
const questionForm = document.getElementById("questionForm");

// Question form submission handler
questionForm.onsubmit = function(e) {
    e.preventDefault();

    const questionText = questionForm.question.value.trim();
    if (!questionText) return;

    const formData = new FormData();
    formData.append("question", questionText);

    fetch("/submit_question", {
        method: "POST",
        body: formData
    })
    .then(r => r.json())
    .then(d => {
        if (d.success) {
            addQuestionToPage(questionText);
            questionForm.reset();
        }
    });
};
// Add a new question to the page
function addQuestionToPage(text) {
    const q = document.createElement("div");
    q.className = "question-item";

    q.innerHTML = `
        <p class="q-text">${text}</p>
        <div class="answer-box" style="display:none;">
            <div class="answers"></div>
            <form class="answerForm">
                <textarea name="answer" placeholder="Write your answer..."></textarea>
                <button type="submit">Submit Answer</button>
            </form>
        </div>
    `;

    if (userRole !== "admin") {
        q.querySelector(".answerForm").style.display = "none";
    }

    // Toggle answer box visibility
    q.querySelector(".q-text").onclick = () => {
        if (userRole !== "admin") {
            alert("Only admins can answer questions.");
            return;
        }

        const box = q.querySelector(".answer-box");
        box.style.display = box.style.display === "none" ? "block" : "none";
    };

    // Handle answer submission
    q.querySelector(".answerForm").onsubmit = (e) => {
        e.preventDefault();
        const ans = e.target.answer.value.trim();
        if (!ans) return;

        const a = document.createElement("div");
        a.textContent = ans;
        q.querySelector(".answers").appendChild(a);

        e.target.reset();
    };

    questionList.prepend(q);
}

/* ====================================
     Community Channel Javascript
===================================== */

// 
const messages = {
    "Life / Workplace Stress": [],
    "Mind & Body Symptoms": [],
    "Motivation": [],
    "Casual Lounge": [],
};

let currentCategory = null;


function openBoard(category) {
    document.getElementById('category-selection').style.display = 'none';
    document.getElementById('board-section').style.display = 'block';
    document.getElementById('board-title').innerText = category;
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
    document.getElementById('message-input').value = '';
}
