import psycopg2
from pprint import pprint

conn = psycopg2.connect(
    database="data_quality", user='postgres', password='secret', host='127.0.0.1', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()

cursor.execute('''SELECT * FROM soda_results''')
results = cursor.fetchall()
pprint(results[-1])
cursor.close()
conn.close()