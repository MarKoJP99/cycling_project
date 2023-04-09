from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# connect to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# define the home page route
@app.route('/')
def home():
    return render_template('home.html')

# define the search results route
@app.route('/results')
def results():
    # get the search query from the form
    query = request.args.get('query')
    
    # search the database for the query
    c.execute('SELECT * FROM table WHERE column LIKE ?', ('%' + query + '%',))
    results = c.fetchall()
    
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
