"""
A simple flask web application to work with Android's WebView.
"""

from flask import Flask, render_template

app = Flask(__name__)

items = [
    {
        'name': "Apples",
        'price': 31.00,
        'quantity': 34
    },
    {
        'name': "Bananas",
        'price': 27.65,
        'quantity': 23
    },
    {
        'name': "Blueberries",
        'price': 35.00,
        'quantity': 20
    },
    {
        'name': "Cinamon",
        'price': 22.50,
        'quantity': 25
    },
    {
        'name': "Honey",
        'price': 26.89,
        'quantity': 12
    },
    {
        'name': "Onions",
        'price': 7.5,
        'quantity': 78
    },
    {
        'name': "Oranges",
        'price': 29.99,
        'quantity': 123
    },
    {
        'name': "Pepper",
        'price': 13.00,
        'quantity': 12
    },
    {
        'name': "Potatoes",
        'price': 40.00,
        'quantity': 34
    }
]

@app.route("/")
def home():
    return render_template('home.html', items=items)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, port=7676)