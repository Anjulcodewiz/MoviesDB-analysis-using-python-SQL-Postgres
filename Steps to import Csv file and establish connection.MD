**Downloaded csv files from provided link**

**Bringing CSV file to necessary format and importing data to Database:**

In downloaded CSV files I did necessary modification in timestamp

I converted timestamp in  ratings.csv using formula: `=(D2 / 86400) + DATE(1970,1,1)` (This formula will return the date in Excel’s standard date/time format.)

also we need to convert it to UTF8 format before uploading it because of several reasons like: data integrity, standardization, special characters, character encoding capability etc.

**Method 1 using PgAdmin 4 to import data**

then in PgAdmin 4 after establishing connection with server(explained in later steps),
Creating database:

following steps : 
Right Click database>create database> selecting necessary details:
![image](https://github.com/Anjulcodewiz/MoviesDB-analysis-using-python-SQL-Postgres/assets/89291748/b90d8458-0213-4478-b3a3-9c23d79dcc54)

OR
using code:  
![image](https://github.com/Anjulcodewiz/MoviesDB-analysis-using-python-SQL-Postgres/assets/89291748/06304efa-a0a1-4c97-afec-9db4f75f2d50)

Then Creating Tables:
**Method 1 creating tables:** 
create table movies and create the respective columns
![image](https://github.com/Anjulcodewiz/MoviesDB-analysis-using-python-SQL-Postgres/assets/89291748/b046e1e3-4fce-4ec2-9cc0-2c142dca7d8b)

create table ratings and create the respective columns
![image](https://github.com/Anjulcodewiz/MoviesDB-analysis-using-python-SQL-Postgres/assets/89291748/b3c224c6-ca0f-4ada-b9c8-17420b70d4a4)

**Method 2 creating tables:**
in query Editor can create tables using this code:

```sql
CREATE TABLE movies (
    id INT PRIMARY KEY,
    title TEXT,
    year INT,
    country TEXT,
    genre TEXT,
    director TEXT,
    minutes INT,
    poster TEXT
);

CREATE TABLE ratings (
    rater_id INT,
    movie_id INT REFERENCES movies(id),
    rating INT,
    time TIMESTAMP
);
```

**Import data from csv file.**

**Method 1 a. :** Right click table > import/ export data> 
Under General: select file path> format (csv.)> Encoding (choose preferred encoding type)

under Options: turn on header> check necessary parameters set by default

Under columns : select necessary column you need to import and select not null columns if data is validated.

**Method 1 b.**
Using code : 

```sql
\copy movies(id, title, year, country, genre, director, minutes, poster) FROM 'C:\\Users\\ANJUL VERMA\\OneDrive\\Desktop\\Movies file downloaded\\movies.csv' DELIMITER ',' CSV HEADER;

\copy ratings(rater_id, movie_id, rating, time) FROM 'C:\\Users\\ANJUL VERMA\\OneDrive\\Desktop\\Movies file downloaded\\ratings.csv' DELIMITER ',' CSV HEADER;
```

In PostgreSQL, the backslash (\\) is a special character, so need to escape it by using double backslashes (\\\\). 

**Method 2: if we are using render (setting up render explained later)**

then in cmd after establishing connection with server(explained in later steps), creating database(explained in later steps) and tables(explained in later steps) we use copy command to import data from csv file. 

and before that we use `SET client_encoding TO ‘UTF8’`:  Used in PostgreSQL to set the client-side encoding (character set) to UTF-8.

further we use copy command to copy files to the tables in their respective columns
![image](https://github.com/Anjulcodewiz/MoviesDB-analysis-using-python-SQL-Postgres/assets/89291748/76463931-5bfb-4a63-8673-b8554a6a83f4)


Using code : 

```sql
\copy movies(id, title, year, country, genre, director, minutes, poster) FROM 'C:\\Users\\ANJUL VERMA\\OneDrive\\Desktop\\Movies file downloaded\\movies.csv' DELIMITER ',' CSV HEADER;



\copy ratings(rater_id, movie_id, rating, time) FROM 'C:\\Users\\ANJUL VERMA\\OneDrive\\Desktop\\Movies file downloaded\\ratings.csv' DELIMITER ',' CSV HEADER;
```

As in PostgreSQL, the backslash (\\) is a special character, so need to escape it by using double backslashes (\\\\).

**Then we need to join tables**
![image](https://github.com/Anjulcodewiz/MoviesDB-analysis-using-python-SQL-Postgres/assets/89291748/848b00fe-e520-4fd1-ba73-96b9a83abca4)

