import psycopg2

def connect_postgresql():
    try:
        connection = psycopg2.connect(
            dbname="mobilerizDB",
            user="postgres",
            password="4628",
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as e:
        print(f"Error: {e}")
        raise