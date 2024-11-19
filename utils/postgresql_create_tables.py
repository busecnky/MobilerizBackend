from config.postgresql_config import connect_postgresql


def create_tables():
    try:
        connection = connect_postgresql()
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            price NUMERIC(10, 2) NOT NULL,
            vendor_id INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendors (
            id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL,
            base_url VARCHAR(255)
        );
        """)

        cursor.execute("""
        ALTER TABLE products ADD CONSTRAINT fk_vendor
        FOREIGN KEY (vendor_id) REFERENCES vendors(id);
        """)

        connection.commit()
        print("Tables created successfully")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()


create_tables()
