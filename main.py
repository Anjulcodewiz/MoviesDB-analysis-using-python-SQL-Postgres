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

# Top 5 Movie Titles considering all criteria
cursor.execute("""
SELECT title, year, minutes, AVG(rating) as avg_rating, COUNT(rating) as num_ratings
FROM movies JOIN ratings ON movies.id = ratings.movie_id
GROUP BY title, year, minutes
HAVING COUNT(rating) >= 5 AND AVG(rating) >= 5
ORDER BY year DESC, minutes DESC, avg_rating DESC, num_ratings DESC
LIMIT 5
""")
top_5_movies = cursor.fetchall()
print("a. Top 5 movies considering: Title, Year, Duration, Average Rating, Number of Ratings")
for movie in top_5_movies:
    print(movie)
print() # adding for a blank line

# Number of Unique Raters
cursor.execute("SELECT COUNT(DISTINCT rater_id) FROM ratings")
num_unique_raters = cursor.fetchone()
print("b. Number of unique raters:", num_unique_raters[0])
print ()

# Top 5 Rater IDs considering all criteria
cursor.execute("""
SELECT rater_id, COUNT(movie_id) as num_movies_rated, AVG(rating) as avg_rating
FROM ratings
GROUP BY rater_id
HAVING COUNT(movie_id) >= 5
ORDER BY num_movies_rated DESC, avg_rating DESC
LIMIT 5
""")
top_5_raters_by_both_criteria = cursor.fetchall()
print("c. Top 5 raters by number of movies rated and highest average rating given: Rater Id, Num of movies rated, Avg rating given", top_5_raters_by_both_criteria)
print()

# Top Rated Movie by 'Michael Bay', 'Comedy', in the year 2013, in India

cursor.execute("""
SELECT title, AVG(rating) as avg_rating
FROM movies JOIN ratings ON movies.id = ratings.movie_id
WHERE director = 'Michael Bay' AND genre = 'Comedy' AND year = 2013 AND country = 'India'
GROUP BY title
HAVING AVG(rating) >= 5
ORDER BY AVG(rating) DESC
LIMIT 1
""")
top_rated_movie = cursor.fetchone()
print("d.Top rated movie by 'Michael Bay', 'Comedy', in the year 2013, in India:", top_rated_movie)
print()

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
print("e. Favorite movie genre of rater ID 1040:", favorite_genre)
print() 

# Favorite Movie Genre of Rater ID 1040
cursor.execute("""
SELECT genre, COUNT(*) as count, AVG(rating) as avg_rating, MIN(rating) as min_rating
FROM movies JOIN ratings ON movies.id = ratings.movie_id
WHERE rater_id = 1040
GROUP BY genre
HAVING AVG(rating) = (SELECT MAX(avg_rating) FROM (
                        SELECT genre, AVG(rating) as avg_rating
                        FROM movies JOIN ratings ON movies.id = ratings.movie_id
                        WHERE rater_id = 1040
                        GROUP BY genre) as subquery)
AND MIN(rating) >= 5
ORDER BY count DESC
LIMIT 1
""")
favorite_genre = cursor.fetchone()
print("f. Favorite movie genre of rater ID 1040 considering highest average rating and minimum rating as 5:", favorite_genre)
print() 

# Year with Second-Highest Number of Action Movies from the USA
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

# Count of Movies with High Ratings
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
print("h. Count of movies with high ratings:", high_rating_movies_count[0]) #(338,), is a tuple. This is because the fetchone() method in psycopg2 returns a single record as a tuple. I used[0]

# Close the cursor and connection
cursor.close()
connection.close()
