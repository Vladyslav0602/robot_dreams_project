// Exercise 2-3
// Генерувати випадкове число від 1 до 100
let randomFriendCount = Math.floor(Math.random() * 100) + 1;

// Оновлення відображення кількості друзів
function updateFriendCount() {
  const countElement = document.getElementById('count');
  countElement.textContent = randomFriendCount;
}

// Ініціалізація кількості друзів при завантаженні сторінки
window.addEventListener('DOMContentLoaded', () => {
  updateFriendCount();
});

// Обробка події натискання на кнопку "Додати в друзі"
const addFriendBtn = document.getElementById('addFriendBtn');
addFriendBtn.addEventListener('click', () => {
  randomFriendCount++; // Збільшення лічильника друзів
  updateFriendCount(); // Оновлення відображення кількості друзів
  addFriendBtn.disabled = true; // Деактивувати кнопку "Додати в друзі"
  addFriendBtn.textContent = 'Очікується підтвердження';
});

// Exercise 4
// Генерування випадкового кольору
function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

// Обробка події натискання на кнопку "Написати повідомлення"
const sendMessageBtn = document.getElementById('sendMessageBtn');
sendMessageBtn.addEventListener('click', () => {
  const currentColor = sendMessageBtn.style.backgroundColor;
  if (currentColor === '') {
    const newColor = getRandomColor();
    sendMessageBtn.style.backgroundColor = newColor;
  } else {
    sendMessageBtn.style.backgroundColor = '';
  }
});

// Exercise 5
// Обробка події натискання на кнопку "Запропонувати роботу"
const offerJobBtn = document.getElementById('offerJobBtn');
offerJobBtn.addEventListener('click', () => {
  const addFriendBtn = document.getElementById('addFriendBtn');
  if (addFriendBtn.style.display === 'none') {
    addFriendBtn.style.display = 'inline-block';
    offerJobBtn.textContent = 'Запропонувати роботу';
  } else {
    addFriendBtn.style.display = 'none';
    offerJobBtn.textContent = 'Запропонувати роботу';
  }
});

// Exercise 6
// Обробка події натискання на кнопку "Здати ДЗ"
const submitHomeworkBtn = document.getElementById('submitHomeworkBtn');
const homeworkTable = document.getElementById('homeworkTable');
submitHomeworkBtn.addEventListener('click', () => {
  const newRow = homeworkTable.insertRow(-1);
  newRow.classList.add('body');
  const newData1 = newRow.insertCell(0);
  newData1.classList.add('exercise');
  const newData2 = newRow.insertCell(1);
  newData2.classList.add('rating');
  newData1.textContent = 'Нове домашнє завдання';
  newData2.textContent = Math.floor(Math.random() * 9); // Рандомна оцінка
});







