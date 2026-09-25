{% extends "base.html" %}

{% block title %}Flakes | {{ movie.title }}{% endblock %}

{% block content %}
<div class="details-container">
    <button class="back-button" onclick="history.back()">← Back</button>
    <div class="details-header">
        <img src="{{ movie.image_url }}" alt="{{ movie.title }}" class="details-poster">
        <div class="details-info">
            <h1>{{ movie.title }}</h1>
            <div class="details-meta">
                <div class="meta-item"><span class="meta-label">Rating:</span> {{ movie.rating }}/10</div>
                <div class="meta-item"><span class="meta-label">Year:</span> {{ movie.year }}</div>
                <div class="meta-item"><span class="meta-label">Type:</span> {{ movie.movie_type }}</div>
                <div class="meta-item"><span class="meta-label">Duration:</span> {{ movie.duration }}</div>
                <div class="meta-item"><span class="meta-label">Genre:</span> {{ movie.genre }}</div>
            </div>
            <p class="details-description">{{ movie.full_description }}</p>
            <div class="details-actions">
                <button class="details-button play-button">▶ Play Now</button>
                <button class="details-button wishlist-button">♥ Add to Wishlist</button>
            </div>
        </div>
    </div>
</div>
{% endblock %}
