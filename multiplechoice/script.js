let data = [];
let currentQuestion = null;
let currentIndex = 0; // Duyệt tuần tự

function loadFromFile() {
    const input = document.getElementById("fileInput");
    const file = input.files[0];

    if (!file) {
        alert("Vui lòng chọn một file .txt!");
        return;
    }

    const reader = new FileReader();
    reader.onload = function (e) {
        const lines = e.target.result
            .split('\n')
            .filter(line => line.includes('–'));
        console.log(lines)
        data = lines.map(line => {
            const [kr, vi] = line.split('–').map(s => s.trim());
            return { korean: kr, meaning: vi };
        });

        if (data.length < 4) {
            alert("File phải có ít nhất 4 dòng.");
            return;
        }

        currentIndex = 0;
        document.getElementById("quiz").style.display = "block";
        document.querySelector(".next").style.display = "inline-block";
        loadQuestion();
    };

    reader.readAsText(file);
}

function loadQuestion() {
    const resultDiv = document.getElementById("result");
    resultDiv.textContent = "";

    if (currentIndex >= data.length) {
        document.getElementById("question").textContent = "🎉 Bạn đã hoàn thành toàn bộ câu hỏi!";
        document.getElementById("choices").innerHTML = "";
        document.querySelector(".next").style.display = "none";
        return;
    }

    currentQuestion = data[currentIndex];
    const correctMeaning = currentQuestion.meaning;

    // Tạo 3 đáp án sai từ các dòng còn lại
    const incorrectChoices = data
        .filter((_, index) => index !== currentIndex)
        .map(d => d.meaning);

    shuffle(incorrectChoices);
    const choices = [correctMeaning, ...incorrectChoices.slice(0, 3)];
    shuffle(choices);

    document.getElementById("question").textContent = currentQuestion.korean;

    const choicesList = document.getElementById("choices");
    choicesList.innerHTML = "";
    choices.forEach(choice => {
        const btn = document.createElement("button");
        btn.textContent = choice;
        btn.className = "choice-btn";
        btn.onclick = () => checkAnswer(choice);
        choicesList.appendChild(btn);
    });
}

function checkAnswer(selected) {
    const result = document.getElementById("result");
    const container = document.querySelector(".quiz-container");
    const gif = document.querySelector(".gif-container");

    if (selected === currentQuestion.meaning) {
        result.textContent = "✅ Chính xác!";
        result.style.color = "green";

        // Hiện ảnh động
        gif.style.display = "block";
        setTimeout(() => {
            gif.style.display = "none";
        }, 1500);
    } else {
        result.textContent = `❌ Sai rồi. Đáp án đúng là: ${currentQuestion.meaning}`;
        result.style.color = "red";

        // Hiệu ứng rung
        container.classList.add("shake");
        setTimeout(() => container.classList.remove("shake"), 500);
    }

    // Chuyển sang câu tiếp theo
    currentIndex++;
}

function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}
