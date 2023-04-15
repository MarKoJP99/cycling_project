class Database:
    def __init__(self):
        self.products = []
    
    def add_product(self, name, description, price, size):
        product = {"name": name, "description": description, "price": price, "size": size}
        self.products.append(product)
    
    def search_products(self, search_term):
        results = []
        for product in self.products:
            if search_term.lower() in product["name"].lower():
                results.append(product)
        return results
