from flask import Flask
from flask import Response, render_template
from models import products

app = Flask(__name__)

# @app.route('/')
# def index():
#     return Response("<h1>Hello, This is home page</h1>")

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)