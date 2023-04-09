import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''CREATE TABLE products (
             id INTEGER PRIMARY KEY,
             name TEXT,
             description TEXT,
             price REAL,
             image TEXT
             )''')

c.execute('''INSERT INTO products (name, description, price, image)
             VALUES ('Road Bike', 'A high-performance road bike for serious cyclists.', 1200.00, 'road-bike.jpg'),
                    ('Mountain Bike', 'A rugged mountain bike for off-road adventures.', 950.00, 'mountain-bike.jpg'),
                    ('City Bike', 'A stylish and practical bike for urban commuters.', 650.00, 'city-bike.jpg'),
                    ('Kids Bike', 'A fun and colorful bike for kids.', 200.00, 'kids-bike.jpg')''')

conn.commit()
conn.close()
