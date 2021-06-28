import time

import psycopg2

while True:
    try:
        conn = psycopg2.connect(
            "host='db' dbname='postgres' user='postgres' password='postgres'"
        )
        break
    except psycopg2.OperationalError:
        time.sleep(1)
