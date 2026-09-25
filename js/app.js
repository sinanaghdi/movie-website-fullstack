* {
  margin: 0;
  box-sizing: border-box;
}

body {
  font-family: "Roboto", sans-serif;
  background: #151515;
  color: white;
}

a {
  color: inherit;
  text-decoration: none;
}

.navbar {
  width: 100%;
  height: 50px;
  background-color: black;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.navbar-container {
  display: flex;
  align-items: center;
  padding: 0 50px;
  height: 100%;
  color: white;
  font-family: "Sen", sans-serif;
}

.logo-container {
  flex: 1;
}

.logo {
  font-size: 30px;
  color: #4dbf00;
  cursor: pointer;
}

.menu-container {
  flex: 6;
}

.menu-list {
  display: flex;
  list-style: none;
  gap: 20px;
}

.menu-list-item {
  cursor: pointer;
  padding: 10px 15px;
  border-bottom: 2px solid transparent;
  transition: 0.3s ease all;
}

.menu-list-item:hover,
.menu-list-item.active {
  color: #4dbf00;
  border-bottom: 2px solid #4dbf00;
  font-weight: bold;
}

.profile-container {
  flex: 2;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 20px;
}

.profile-text-container {
  display: flex;
  align-items: center;
  gap: 5px;
}

.profile-picture {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  object-fit: cover;
}

.toggle {
  width: 40px;
  height: 20px;
  background-color: white;
  border-radius: 30px;
  display: flex;
  align-items: center;
  justify-content: space-around;
  position: relative;
  cursor: pointer;
}

.toggle-icon {
  color: goldenrod;
  font-size: 12px;
}

.toggle-ball {
  width: 18px;
  height: 18px;
  background-color: black;
  position: absolute;
  right: 1px;
  border-radius: 50%;
  transition: 0.3s ease all;
}

.sidebar {
  width: 50px;
  height: 100%;
  background-color: black;
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 60px;
  z-index: 999;
}

.left-menu-icon {
  color: white;
  font-size: 20px;
  margin-bottom: 40px;
  cursor: pointer;
}

.container {
  background-color: #151515;
  min-height: calc(100vh - 50px);
  color: white;
}

.content-container {
  margin-left: 50px;
  padding-bottom: 50px;
}

.featured-content {
  height: 50vh;
  padding: 50px;
  background-size: cover;
  background-position: center;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}

.featured-title {
  width: 200px;
  margin-bottom: 20px;
}

.featured-desc {
  width: 500px;
  color: lightgray;
  margin: 30px 0;
  line-height: 1.6;
}

.featured-button {
  background-color: #4dbf00;
  color: white;
  padding: 10px 20px;
  border-radius: 10px;
  border: none;
  outline: none;
  font-weight: bold;
  width: fit-content;
  transition: 0.3s ease all;
}

.featured-button:hover {
  background-color: #3a9400;
}

.movie-list-container {
  padding: 20px 20px;
}

.movie-list-title {
  margin: 20px 0;
  font-size: 24px;
}

.movie-list-wrapper {
  position: relative;
  overflow: hidden;
}

.movie-list {
  display: flex;
  align-items: center;
  height: 300px;
  transform: translateX(0);
  transition: all 0.5s ease-in-out;
  gap: 20px;
}

.movie-list-item {
  position: relative;
  flex-shrink: 0;
}

.movie-list-item:hover .movie-list-item-img {
  transform: scale(1.2);
  opacity: 0.5;
}

.movie-list-item:hover .movie-list-item-title,
.movie-list-item:hover .movie-list-item-desc,
.movie-list-item:hover .movie-list-item-button {
  opacity: 1;
}

.movie-list-item-img {
  transition: all 0.3s ease-in-out;
  width: 270px;
  height: 200px;
  object-fit: cover;
  border-radius: 20px;
  cursor: pointer;
}

.movie-list-item-title {
  background-color: rgba(51, 51, 51, 0.9);
  padding: 0 10px;
  font-size: 24px;
  font-weight: bold;
  position: absolute;
  top: 10%;
  left: 50px;
  opacity: 0;
  transition: 0.3s all ease-in-out;
}

.movie-list-item-desc {
  background-color: rgba(51, 51, 51, 0.9);
  padding: 10px;
  font-size: 14px;
  position: absolute;
  top: 30%;
  left: 50px;
  width: 230px;
  opacity: 0;
  transition: 0.3s all ease-in-out;
}

.movie-list-item-button {
  padding: 8px 15px;
  background-color: #4dbf00;
  color: white;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  position: absolute;
  bottom: 20px;
  left: 50px;
  opacity: 0;
  transition: 0.3s all ease-in-out;
  font-weight: bold;
}

.arrow {
  font-size: 50px;
  position: absolute;
  top: 50%;
  right: 20px;
  color: #4dbf00;
  opacity: 0.7;
  cursor: pointer;
  transform: translateY(-50%);
}

.page-header {
  padding: 40px 20px;
  text-align: center;
}

.page-title {
  font-size: 48px;
  margin-bottom: 30px;
  font-weight: bold;
}

.filter-container {
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
}

.search-box,
.genre-filter {
  padding: 12px 20px;
  border-radius: 25px;
  border: 2px solid #4dbf00;
  background-color: #1a1a1a;
  color: white;
  width: 300px;
  font-size: 14px;
}

.movies-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  padding: 20px;
}

.movie-card {
  position: relative;
  border-radius: 15px;
  overflow: hidden;
  cursor: pointer;
  transition: 0.3s ease all;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
}

.movie-card:hover {
  transform: translateY(-10px);
}

.movie-card img {
  width: 100%;
  height: 300px;
  object-fit: cover;
}

.movie-card-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  opacity: 0;
  transition: 0.3s ease all;
}

.movie-card:hover .movie-card-overlay {
  opacity: 1;
}

.movie-card-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
}

.movie-card-rating {
  font-size: 16px;
  color: #4dbf00;
  margin-bottom: 15px;
}

.movie-card-button {
  padding: 10px 25px;
  background-color: #4dbf00;
  color: white;
  border: none;
  border-radius: 5px;
  font-weight: bold;
}

.details-container {
  padding: 40px 20px;
}

.details-header {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 40px;
  margin-bottom: 40px;
}

.details-poster {
  width: 100%;
  max-width: 300px;
  border-radius: 15px;
}

.details-info h1 {
  font-size: 48px;
  margin-bottom: 20px;
}

.details-meta {
  display: flex;
  gap: 20px;
  margin: 20px 0;
  flex-wrap: wrap;
}

.meta-item {
  padding: 8px 15px;
  background-color: #1a1a1a;
  border-radius: 5px;
}

.meta-label {
  color: #4dbf00;
  font-weight: bold;
}

.details-description {
  font-size: 16px;
  line-height: 1.8;
  color: lightgray;
  margin: 20px 0;
}

.details-actions {
  display: flex;
  gap: 15px;
  margin-top: 30px;
}

.details-button {
  padding: 12px 30px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  font-size: 16px;
}

.play-button {
  background-color: #4dbf00;
  color: white;
}

.wishlist-button {
  background-color: #1a1a1a;
  color: white;
  border: 2px solid #4dbf00;
}

.back-button {
  padding: 10px 20px;
  background-color: #1a1a1a;
  color: white;
  border: 2px solid #4dbf00;
  border-radius: 5px;
  cursor: pointer;
  margin-bottom: 20px;
}

.empty-state {
  text-align: center;
  padding: 40px;
}

@media only screen and (max-width: 940px) {
  .menu-container { display: none; }
  .movies-grid { grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); }
}
