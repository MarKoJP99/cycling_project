from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results')
def results():
    query = request.args.get('query')
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM products WHERE name LIKE '%{query}%' OR description LIKE '%{query}%'")
    products = cursor.fetchall()
    conn.close()
    return render_template('results.html', products=products)

@app.route('/all')
def all():
    print("Inside all_products function")
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    return render_template('all.html', products=rows)




if __name__ == '__main__':
    app.run(debug=True)
