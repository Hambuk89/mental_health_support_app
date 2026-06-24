/* ==================================
          Q&A Forum Javascript
================================== */

if (document.getElementById("questionForm")) {

    const questionList = document.getElementById("questionList");
    const questionForm = document.getElementById("questionForm");

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
                window.location.reload();
            }
        });
    };

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

        q.querySelector(".q-text").onclick = () => {
            if (userRole !== "admin") {
                alert("Only admins can answer questions.");
                return;
            }

            const box = q.querySelector(".answer-box");
            box.style.display = box.style.display === "none" ? "block" : "none";
        };

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
}
