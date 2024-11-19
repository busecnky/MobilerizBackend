import sqlite3
import psycopg2

from config.sqlite_config import DATABASE_URL


def sync_sqlite_to_postgres():
    global pg_conn, sqlite_conn, sqlite_cursor, pg_cursor

    try:
        sqlite_conn = sqlite3.connect(DATABASE_URL)
        sqlite_cursor = sqlite_conn.cursor()

        pg_conn = psycopg2.connect(
            dbname='mobilerizDB',
            user='postgres',
            password='4628',
            host='localhost',
            port='5432'
        )
        pg_cursor = pg_conn.cursor()

        sqlite_cursor.execute("SELECT * FROM products WHERE synced = 0")
        rows = sqlite_cursor.fetchall()

        for row in rows:
            pg_cursor.execute(
                """
                INSERT INTO products (name, description, price, vendor_id)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (row[1], row[2], row[3], row[4])
            )

            # Senkronize edilmiş olarak işaretle
            sqlite_cursor.execute(
                "UPDATE products SET synced = 1 WHERE id = ?", (row[0],)
            )

        sqlite_conn.commit()
        pg_conn.commit()

    except Exception as e:
        print(f"Error during sync: {e}")
        if 'pg_conn' in locals():
            pg_conn.rollback()
        if 'sqlite_conn' in locals():
            sqlite_conn.rollback()

    finally:
        if 'sqlite_cursor' in locals():
            sqlite_cursor.close()
        if 'sqlite_conn' in locals():
            sqlite_conn.close()
        if 'pg_cursor' in locals():
            pg_cursor.close()
        if 'pg_conn' in locals():
            pg_conn.close()
