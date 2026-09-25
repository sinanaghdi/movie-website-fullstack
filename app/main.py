document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.toggle');
  const toggleBall = document.querySelector('.toggle-ball');
  const arrows = document.querySelectorAll('.arrow');
  const movieLists = document.querySelectorAll('.movie-list');

  if (toggle && toggleBall) {
    toggle.addEventListener('click', () => {
      toggleBall.classList.toggle('active');
      document.body.classList.toggle('light-mode');
      const elements = document.querySelectorAll('.container, .navbar, .sidebar, .movie-list-title, .movie-card, .search-box, .genre-filter');
      elements.forEach(el => el.classList.toggle('light-mode'));
    });
  }

  arrows.forEach((arrow, index) => {
    let clickCounter = 0;
    const list = movieLists[index];
    if (!list) return;

    const images = list.querySelectorAll('.movie-list-item');
    arrow.addEventListener('click', () => {
      const ratio = Math.floor(window.innerWidth / 270);
      clickCounter++;

      if (images.length - (4 + clickCounter) + (4 - ratio) >= 0) {
        list.style.transform = `translateX(${clickCounter * -300}px)`;
      } else {
        list.style.transform = 'translateX(0)';
        clickCounter = 0;
      }
    });
  });
});

window.addEventListener('resize', () => {
  const lists = document.querySelectorAll('.movie-list');
  lists.forEach(list => {
    list.style.transform = 'translateX(0)';
  });
});
