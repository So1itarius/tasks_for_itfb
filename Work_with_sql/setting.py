import psycopg2

path = "data-3895-2019-11-30.json"

con = psycopg2.connect(
    database="testdb3",
    user="postgres",
    password="p250809101009",
    host="localhost",
    port="5432"
)