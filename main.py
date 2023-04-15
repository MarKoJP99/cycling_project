from database import Database
from website import Website

# Initialize the database with some sample products
database = Database()
database.add_product("Bike1", "A fast and lightweight bike", 1000, "M")
database.add_product("Bike2", "A sturdy mountain bike", 1500, "L")
database.add_product("Bike3", "A stylish city bike", 800, "S")
database.add_product("Bike4", "A comfortable touring bike", 1200, "XL")

# Initialize the website with the database
website = Website(database)

# Start the website
website.start()
