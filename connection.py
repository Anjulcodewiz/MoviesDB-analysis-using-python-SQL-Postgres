import psycopg2

# checked connection with postgres database
connection = psycopg2.connect(
    host="localhost",
    database="MoviesDB",
    user="postgres",
    password="Ram$Anjul",
    port = "5432"
)