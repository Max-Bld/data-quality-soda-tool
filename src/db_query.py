import psycopg2
from pprint import pprint
import json

def get_last_results():
    conn = psycopg2.connect(
        database="data_quality", user='postgres', password='secret', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM soda_results''')
    results = cursor.fetchall()[-1][0]
    cursor.close()
    conn.close()

    return results