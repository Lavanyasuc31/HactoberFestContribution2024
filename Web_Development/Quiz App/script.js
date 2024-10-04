const audio = new Audio("click.mp3");

const alert = document.getElementById('alert');
const homeContainer = document.getElementById('home-container');
const quizContainer = document.getElementById('quiz-container');
const submitBtn = document.getElementById('submit-btn');
const queBox = document.getElementById('queBox');
const optionInput = document.querySelectorAll('.options');
const allLabel = document.getElementsByTagName('label');
const arrLabel = Array.from(allLabel);
let questions;

function startQuiz(type) {
  if (type == "cricket") {
    questions = cricketQuestions;
    loadQuestion();
  } else if (type == "coding") {
    questions = codingQuestions;
    loadQuestion();
  } else if (type == "history") {
    questions = historyQuestions;
    loadQuestion();
  } else {
    console.log("Do nothing");
  }
}

let index = 0;
let right = 0;
let wrong = 0;

// Function to reset label background colors
function resetLabelBackgroundColors() {
  arrLabel.forEach((option) => {
    option.style.backgroundColor = "";
  });
}

function loadQuestion() {
  homeContainer.style.display = "none";
  quizContainer.style.display = "block";

  // Reset label background colors
  resetLabelBackgroundColors();

  if (index === questions.length) {
    return endQuiz();
  }
  reset();
  const data = questions[index];
  queBox.innerText = `${index + 1}. ${data.Que}`;
  optionInput[0].nextElementSibling.innerText = data.a;
  optionInput[1].nextElementSibling.innerText = data.b;
  optionInput[2].nextElementSibling.innerText = data.c;
  optionInput[3].nextElementSibling.innerText = data.d;
}

const endQuiz = () => {
  if (right >= 6) {
    document.getElementById('quiz-container').innerHTML = `
    <div class="text-center p-4">
      <h3 class="text-success">Thank you for playing the quiz!!</h3>
      <h5>${right}/10 are correct</h5>
      <a href="index.html">Home</a>
    </div>
    `;
  } else {
    document.getElementById('quiz-container').innerHTML = `
    <div class="text-center p-4">
      <h3 class="text-success">Thank you for playing the quiz!!</h3>
      <h5>${right}/10 are correct</h5>
      <a href="index.html">Home</a>
    </div>
    `;
  }
}

const reset = () => {
  optionInput.forEach((input) => {
    input.checked = false;
  });
}

const getAnswer = () => {
  let answer;
  optionInput.forEach((input) => {
    if (input.checked) {
      answer = input.value;
    }
  });
  return answer;
}

submitBtn.addEventListener('click', () => {
  audio.play();
  submitQuiz();
});

const submitQuiz = () => {
  const data = questions[index];
  const ans = getAnswer();
  if (ans == undefined) {
   
    alert.innerHTML = "Please select any option.";
    
  } else {
    document.getElementById("submit-btn").disabled = true;
    if (ans === data.Answer) {
      right++;
      
      alert.innerHTML = "Correct Answer.";
      
    } else {
      
      alert.innerHTML = "Wrong Answer, the correct answer is " + data.Answer;
     
      wrong++;
    }
    setTimeout(() => {
      alert.innerHTML="Please select any option"
      index++;
      loadQuestion();
      submitBtn.disabled = false;
    }, 1000);
  }
  return;
}

arrLabel.forEach((label) => {
  label.addEventListener('click', () => {
    arrLabel.forEach((option) => {
      option.style.backgroundColor = "";
    });
    label.style.backgroundColor = "#27ae60";
  });
});
