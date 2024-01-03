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
# a.1: Top 5 Movie Titles by Duration (minutes)
cursor.execute("SELECT title FROM movies ORDER BY minutes DESC LIMIT 5")
top_5_movies_by_duration = cursor.fetchall()
print("a.1: Top 5 movies by duration:", top_5_movies_by_duration)
print()

# a.2: Top 5 Movie Titles by Year of Release
cursor.execute("SELECT title FROM movies ORDER BY year DESC LIMIT 5")
top_5_movies_by_year = cursor.fetchall()
print("a.2: Top 5 movies by year of release:", top_5_movies_by_year)
print()

# a.3: Top 5 Movie Titles by Average Rating
cursor.execute("""
SELECT title, AVG(rating) as avg_rating
FROM movies JOIN ratings ON movies.id = ratings.movie_id
GROUP BY title
HAVING COUNT(rating) >= 5
ORDER BY avg_rating DESC
LIMIT 5
""")
top_5_movies_by_avg_rating = cursor.fetchall()
print("a.3: Top 5 movies by average rating:", top_5_movies_by_avg_rating)
print()

# a.4: Top 5 Movie Titles by Number of Ratings Given
cursor.execute("""
SELECT title, COUNT(rating) as num_ratings
FROM movies JOIN ratings ON movies.id = ratings.movie_id
GROUP BY title
ORDER BY num_ratings DESC
LIMIT 5
""")
top_5_movies_by_num_ratings = cursor.fetchall()
print("a.4: Top 5 movies by number of ratings given:", top_5_movies_by_num_ratings)
print()

# b: Number of Unique Raters
cursor.execute("SELECT COUNT(DISTINCT rater_id) FROM ratings")
num_unique_raters = cursor.fetchone()
print("b: Number of unique raters:", num_unique_raters[0])
print()

# c.1: Top 5 Rater IDs by Most Movies Rated
cursor.execute("""
SELECT rater_id, COUNT(movie_id) as num_movies_rated
FROM ratings
GROUP BY rater_id
ORDER BY num_movies_rated DESC
LIMIT 5
""")
top_5_raters_by_num_movies = cursor.fetchall()
print("c.1: Top 5 raters by number of movies rated:", top_5_raters_by_num_movies)
print()

# c.2: Top 5 Rater IDs by Highest Average Rating Given
cursor.execute("""
SELECT rater_id, AVG(rating) as avg_rating
FROM ratings
GROUP BY rater_id
HAVING COUNT(movie_id) >= 5
ORDER BY avg_rating DESC
LIMIT 5
""")
top_5_raters_by_avg_rating = cursor.fetchall()
print("c.2: Top 5 raters by highest average rating given:", top_5_raters_by_avg_rating)
print()

# d.1: Director 'Michael Bay'
cursor.execute("""
SELECT title, AVG(rating) as avg_rating
FROM movies 
JOIN ratings ON movies.id = ratings.movie_id
WHERE director = 'Michael Bay'
GROUP BY title
HAVING COUNT(rating) >= 5
ORDER BY avg_rating DESC
LIMIT 1
""")
top_rated_movie_bay = cursor.fetchone()
print("d.1: Top rated movie by Michael Bay:", top_rated_movie_bay)
print()

# d.2: 'Comedy'
cursor.execute("""
SELECT title, AVG(rating) as avg_rating
FROM movies 
JOIN ratings ON movies.id = ratings.movie_id
WHERE genre = 'Comedy'
GROUP BY title
HAVING COUNT(rating) >= 5
ORDER BY avg_rating DESC
LIMIT 1
""")
top_rated_movie_comedy = cursor.fetchone()
print("d.2: Top rated comedy movie:", top_rated_movie_comedy)
print()

# d.3: In the year 2013
cursor.execute("""
SELECT title, AVG(rating) as avg_rating
FROM movies 
JOIN ratings ON movies.id = ratings.movie_id
WHERE year = 2013
GROUP BY title
HAVING COUNT(rating) >= 5
ORDER BY avg_rating DESC
LIMIT 1
""")
top_rated_movie_2013 = cursor.fetchone()
print("d.3: Top rated movie in 2013:", top_rated_movie_2013)
print()

# d.4: In India
cursor.execute("""
SELECT title, AVG(rating) as avg_rating
FROM movies 
JOIN ratings ON movies.id = ratings.movie_id
WHERE country = 'India'
GROUP BY title
HAVING COUNT(rating) >= 5
ORDER BY avg_rating DESC
LIMIT 1
""")
top_rated_movie_india = cursor.fetchone()
print("d.4: Top rated movie in India:", top_rated_movie_india)
print()

# e. Favorite Movie Genre of Rater ID 1040
cursor.execute("""
SELECT genre, COUNT(*) as count
FROM ratings
JOIN movies ON movies.id = ratings.movie_id
WHERE rater_id = 1040
GROUP BY genre
ORDER BY count DESC
LIMIT 1
""")
favorite_genre = cursor.fetchone()
print("e: Favorite movie genre of rater with ID 1040:", favorite_genre[0])
print()

# f. Highest Average Rating for a Movie Genre by Rater ID 1040
cursor.execute("""
SELECT genre, AVG(rating) as avg_rating
FROM ratings
JOIN movies ON movies.id = ratings.movie_id
WHERE rater_id = 1040
GROUP BY genre
HAVING COUNT(rating) >= 5
ORDER BY avg_rating DESC
LIMIT 1
""")
highest_avg_rating_genre = cursor.fetchone()
print("f: Highest average rating for a movie genre by rater with ID 1040:", highest_avg_rating_genre)
print()

# g: Year with Second-Highest Number of Action Movies from the USA
cursor.execute("""
WITH movie_avg_rating AS (
    SELECT year, movie_id, AVG(rating) as avg_rating
    FROM movies JOIN ratings ON movies.id = ratings.movie_id
    WHERE genre = 'Action' AND country = 'USA' AND minutes < 120
    GROUP BY year, movie_id
),
filtered_movies AS (
    SELECT year
    FROM movie_avg_rating
    WHERE avg_rating >= 6.5
)
SELECT year, COUNT(*) as count
FROM filtered_movies
GROUP BY year
ORDER BY count DESC
OFFSET 1
LIMIT 1
""")
second_highest_action_movies_year = cursor.fetchone()
print("g. Year with second-highest number of action movies from the USA with average rating of 6.5 or higher and runtime of less than 120 minutes:", second_highest_action_movies_year)
print()

# h. Count of Movies with High Ratings
cursor.execute("""
SELECT COUNT(*)
FROM (
    SELECT movie_id
    FROM ratings
    WHERE rating >= 7
    GROUP BY movie_id
    HAVING COUNT(rating) >= 5
) as high_rating_movies
""")
high_rating_movies_count = cursor.fetchone()
print("h. Count of movies with high ratings:", high_rating_movies_count[0])

# Close the cursor and connection
cursor.close()
connection.close()
