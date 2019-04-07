from flask import Flask, render_template, request
from app import app


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/search_results')
def search_results():
    return render_template("search_results.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
