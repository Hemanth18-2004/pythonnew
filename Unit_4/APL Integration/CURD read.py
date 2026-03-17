import psycopg2 as psy

# Connect to the college Database
conn = psy.connect(
    dbname = 'College',
    user = 'postgres',
    password = 'vaibhavhinduja',
    host = 'localhost',
    port = '5432'
)
