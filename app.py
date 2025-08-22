from flask import *
import secrets

app = Flask(__name__)
app.secret_key = 'LucasAmateDev'

@app.route('/')

def home():
    return render_template("home.html")

@app.route('/news')

def news():
    return render_template("news.html")

@app.route('/articles')

def articles():
    return render_template("articles.html")

if __name__ == '__main__':
    app.run(debug=True)