import psycopg2
from soda_pandas import j

conn = psycopg2.connect(
    database="data_quality", user='postgres', password='secret', host='127.0.0.1', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()

cursor.execute(f'''INSERT INTO soda_results(results) VALUES ('{j}')''')

cursor.close()
conn.close()