# Insights and Analysis assumptions:

In the CSV file, certain movies are listed with a duration of 0 minutes, no director name, no poster, no country, and no genre. It is assumed that these omissions are due to errors in data capture, and the data is processed with this assumption in mind.

a.	Assumptions in Top 5 Movie Titles:
The movies are sorted by year (newest first), duration (longest first), average rating (highest first with minimum avg 5 star), and number of ratings (highest first)

b.	No assumptions : Number of Unique Raters.

c.	Assumptions: Top 5 Rater IDs: Sort and print the top 5 rater IDs based on: 
-The rater has rated at least 5 movies.
-The raters are sorted by the number of movies they’ve rated (most first) and their average      rating given (highest first).

d.  Assumptions: Top Rated Movie: 
-Top-rated movie by ‘Michael Bay’, in the ‘Comedy’ genre, in the year 2013, in India.
-The average rating of the movie is at least 5.

e. No assumptions: The genre of the movies that the rater with ID 1040 has rated the most.

f.  Assumptions: Highest Average Rating for a Movie Genre by Rater ID 1040:
-The genre of the movies that the rater with ID 1040 has rated the most.
-The average rating given by the rater to the movies genre is highest among all genres rated     by the rater.
-The minimum rating given by the rater to the movies of this genre is at least 5.

g. No assumptions: Year with Second-Highest Number of Action Movies

h. No assumptions: Count of Movies with High Ratings
 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Task Overview:
1. Data Import:
- Set up a PostgreSQL database. (You can setup a free PostgreSQL instance from Render)
- Create tables to store movie and rating data from the CSV files
(You can download the CSV files from here)
- Import the CSV data into the respective tables in the PostgreSQL database.
2. Insights and Analysis:
- Use any scripting language of your choice (e.g., Python, Javascript, etc.) to perform the
following insights:
a. Top 5 Movie Titles: Sort and print the top 5 movie titles based on the following criteria:
● Duration
● Year of Release
● Average rating (consider movies with minimum 5 ratings)
● Number of ratings given
b. Number of Unique Raters: Determine and print the count of unique rater IDs.
c. Top 5 Rater IDs: Sort and print the top 5 rater IDs based on:
● Most movies rated
● Highest Average rating given (consider raters with min 5 ratings)
d. Top Rated Movie:
- Find and print the top-rated movies by:
● Director 'Michael Bay',
● 'Comedy',
● In the year 2013
● In India (consider movies with a minimum of 5 ratings).
e. Favorite Movie Genre of Rater ID 1040: Determine and print the favorite movie genre
for the rater with ID 1040 (defined as the genre of the movie the rater has rated most often).
f. Highest Average Rating for a Movie Genre by Rater ID 1040: Find and print the
highest average rating for a movie genre given by the rater with ID 1040 (consider genres with a
minimum of 5 ratings).
g. Year with Second-Highest Number of Action Movies: Identify and print the year with
the second-highest number of action movies from the USA that received an average rating of
6.5 or higher and had a runtime of less than 120 minutes.
h. Count of Movies with High Ratings: Count and print the number of movies that have
received at least five reviews with a rating of 7 or higher.
3. Language and Tools:
- You can use any scripting language and appropriate tools/libraries to accomplish the tasks
efficiently.
4. Submission:
- Please present your solution by uploading it to GitHub and and share the repository link with
us.
- Additionally, include any assumptions made during the process and comments to explain
the logic of your code
------------------------------------------------------------------------------------------------------------------------------------------------------------------
