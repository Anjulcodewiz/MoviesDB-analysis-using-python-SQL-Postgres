import psycopg2

# Establish a connection to the database
connection = psycopg2.connect(
    host="localhost",
    database="MoviesDB",
    user="postgres",
    password="Ram$Anjul",
    port = "5432"
)

# Create a cursor object
cursor = connection.cursor()


# Number of Unique Raters
cursor.execute("SELECT COUNT(DISTINCT rater_id) FROM ratings")
num_unique_raters = cursor.fetchone()
print("Number of unique raters:", num_unique_raters[0])
print ()

# Top 5 Rater IDs by Most Movies Rated
cursor.execute("""
SELECT rater_id, COUNT(movie_id) as num_movies_rated
FROM ratings
GROUP BY rater_id
ORDER BY num_movies_rated DESC
LIMIT 5
""")
top_5_raters_by_num_movies = cursor.fetchall()
print("Top 5 raters by number of movies rated:", top_5_raters_by_num_movies)
print()

# Top 5 Rater IDs by Highest Average Rating Given
cursor.execute("""
SELECT rater_id, AVG(rating) as avg_rating
FROM ratings
GROUP BY rater_id
HAVING COUNT(movie_id) >= 5
ORDER BY avg_rating DESC
LIMIT 5
""")
top_5_raters_by_avg_rating = cursor.fetchall()
print("Top 5 raters by highest average rating given:", top_5_raters_by_avg_rating)
print()

# Top Rated Movie by 'Michael Bay', 'Comedy', in the year 2013, in India
cursor.execute("""
SELECT title, AVG(rating) as avg_rating
FROM movies JOIN ratings ON movies.id = ratings.movie_id
WHERE director = 'Michael Bay' AND genre = 'Comedy' AND year = 2013 AND country = 'India'
GROUP BY title
HAVING COUNT(rating) >= 5
ORDER BY avg_rating DESC
LIMIT 1
""")
top_rated_movie = cursor.fetchone()
print("Top rated movie by 'Michael Bay', 'Comedy', in the year 2013, in India:", top_rated_movie)

# Favorite Movie Genre of Rater ID 1040
cursor.execute("""
SELECT genre, COUNT(*) as count
FROM movies JOIN ratings ON movies.id = ratings.movie_id
WHERE rater_id = 1040
GROUP BY genre
ORDER BY count DESC
LIMIT 1
""")
print()
favorite_genre = cursor.fetchone()
print("Favorite movie genre of rater ID 1040:", favorite_genre)

# Highest Average Rating for a Movie Genre by Rater ID 1040
cursor.execute("""
SELECT genre, AVG(rating) as avg_rating
FROM movies JOIN ratings ON movies.id = ratings.movie_id
WHERE rater_id = 1040
GROUP BY genre
HAVING COUNT(rating) >= 5
ORDER BY avg_rating DESC
LIMIT 1
""")
highest_avg_rating_genre = cursor.fetchone()
print("Highest average rating for a movie genre by rater ID 1040:", highest_avg_rating_genre)
print()

# Year with Second-Highest Number of Action Movies from the USA
cursor.execute("""
SELECT year, COUNT(*) as count
FROM movies
WHERE genre = 'Action' AND country = 'USA' AND minutes < 120
GROUP BY year
ORDER BY count DESC
OFFSET 1
LIMIT 1
""")
second_highest_action_movies_year = cursor.fetchone()
print("Year with second-highest number of action movies from the USA:", second_highest_action_movies_year)
print()

# Count of Movies with High Ratings
cursor.execute("""
SELECT COUNT(DISTINCT movie_id)
FROM ratings
WHERE rating >= 7
GROUP BY movie_id
HAVING COUNT(rating) >= 5
""")
high_rating_movies_count = cursor.fetchone()
print("Count of movies with high ratings:", high_rating_movies_count)

# Close the cursor and connection
cursor.close()
connection.close()
