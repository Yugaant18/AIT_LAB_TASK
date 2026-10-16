
# Knowledge-Based Movie Recommendation System

# User preferences
preferred_genres = {"Science Fiction", "Adventure"}
watched_titles = {"Interstellar", "Dune"}
rewatching = False

# Knowledge base
movies = [
    {
        "title": "The Martian",
        "genres": {"Science Fiction", "Adventure"},
        "themes": {"Space", "Survival"},
        "rating": 4.8,
        "available": True
    },
    {
        "title": "Gravity",
        "genres": {"Science Fiction", "Drama"},
        "themes": {"Space", "Survival"},
        "rating": 4.5,
        "available": True
    },
    {
        "title": "Foundation",
        "genres": {"Science Fiction", "Drama"},
        "themes": {"Space", "Politics"},
        "rating": 4.6,
        "available": False
    },
    {
        "title": "Interstellar",
        "genres": {"Science Fiction", "Adventure"},
        "themes": {"Space", "Exploration"},
        "rating": 5.0,
        "available": True
    },
    {
        "title": "Dune",
        "genres": {"Science Fiction", "Adventure"},
        "themes": {"Space", "Politics"},
        "rating": 4.0,
        "available": True
    }
]

# Relevant themes from viewing history
preferred_themes = {"Space", "Survival"}

recommendations = []

# Apply knowledge-based reasoning
for movie in movies:

    if not movie["available"]:
        continue

    if not rewatching and movie["title"] in watched_titles:
        continue

    matched_genres = movie["genres"] & preferred_genres
    matched_themes = movie["themes"] & preferred_themes

    if matched_genres or matched_themes:

        G = len(matched_genres) / len(preferred_genres)
        T = len(matched_themes) / len(preferred_themes)
        R = movie["rating"] / 5
        H = 1 if matched_themes else 0

        score = 4 * G + 3 * T + 2 * R + H

        reason = (
            "Matches preferred genres and themes"
            if matched_genres and matched_themes
            else "Matches some preferred interests"
        )

        recommendations.append(
            (movie["title"], score, reason)
        )

# Sort by score, highest first
recommendations.sort(key=lambda x: x[1], reverse=True)

# Display results
print("KNOWLEDGE-BASED MOVIE RECOMMENDATIONS")
print("-------------------------------------")
print("Preferred Genres:", ", ".join(sorted(preferred_genres)))
print("\nRecommended Movies:\n")

if recommendations:
    for title, score, reason in recommendations:
        print("Movie:", title)
        print("Score:", round(score, 2))
        print("Reason:", reason)
        print()
else:
    print("No suitable movies found.")