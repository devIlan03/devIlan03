let users = [];
let currentIndex = 0;
let liked = [];

function loadUsers() {
  fetch('../data/users.json')
    .then((response) => response.json())
    .then((data) => {
      users = data;
      initMap();
      showNext();
    });
}

function initMap() {
  const map = L.map('map').setView([-23.561684, -46.625378], 4);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }).addTo(map);

  users.forEach((user) => {
    const marker = L.marker([user.lat, user.lng]).addTo(map);
    marker.bindPopup(`<b>${user.name}</b>`);
  });
}

function showNext() {
  const card = document.getElementById('card');
  card.innerHTML = '';
  if (currentIndex >= users.length) {
    card.textContent = 'Nenhum usuário restante.';
    return;
  }
  const user = users[currentIndex];
  const div = document.createElement('div');
  div.className = 'profile';
  div.innerHTML = `
    <img src="${user.photo}" alt="${user.name}">
    <h2>${user.name}, ${user.age}</h2>
    <p>${user.bio}</p>
  `;
  const btnContainer = document.createElement('div');
  btnContainer.className = 'buttons';
  const likeBtn = document.createElement('button');
  likeBtn.textContent = 'Curtir';
  likeBtn.onclick = () => {
    liked.push(user);
    currentIndex++;
    showNext();
  };
  const passBtn = document.createElement('button');
  passBtn.textContent = 'Passar';
  passBtn.onclick = () => {
    currentIndex++;
    showNext();
  };
  btnContainer.appendChild(likeBtn);
  btnContainer.appendChild(passBtn);
  div.appendChild(btnContainer);
  card.appendChild(div);
}

document.addEventListener('DOMContentLoaded', loadUsers);
