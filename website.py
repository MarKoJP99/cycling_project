from flask import Flask, render_template, request, redirect, url_for

class Website:
    def __init__(self, database):
        self.database = database
        self.app = Flask(__name__)
        
        @self.app.route("/")
        def home():
            return render_template("home.html")
        
        @self.app.route("/search")
        def search():
            search_term = request.args.get("q")
            results = self.database.search_products(search_term)
            if results:
                return render_template("results.html", results=results)
            else:
                return render_template("no_results.html")
        
        @self.app.route("/back")
        def back():
            return redirect(url_for("home"))
    
    def start(self):
        self.app.run()
