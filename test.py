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
print("Year with second-highest number of action movies from the USA with average rating of 6.5 or higher and runtime of less than 120 minutes:", second_highest_action_movies_year)


# Close the cursor and connection
cursor.close()
connection.close()

#Path of folderC:\Users\ANJUL VERMA\OneDrive\Desktop\Python work\main.py