"""
Store Inventory routes.
"""
from flask import flash, render_template, redirect, url_for
import requests

from storeinventory import app
from storeinventory.forms import ItemInformationForm

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


@app.route("/", methods=['GET'])
def home():

    response = requests.get("http://127.0.0.1:7776/")
    if response.status_code == 200:
        flash("Items fetched successfully", category='success')
        items =  response.json()
    else:
        flash("Items not fetched", category='failure')
        items = []

    return render_template('home.html', items=items)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/edit", methods=['GET', 'POST'])
def edit_item():
    form = ItemInformationForm()

    if form.validate_on_submit():
        flash('Item info updated.', 'success')

        return redirect(url_for('home'))

    return render_template('edit.html', title='Edit Item', form=form)


@app.route("/add", methods=['GET', 'POST'])
def add_item():
    form = ItemInformationForm()

    if form.validate_on_submit():
        flash('New item added to inventory.', 'success')

        return redirect(url_for('home'))

    return render_template('add.html', title='Add Item', form=form)


@app.route("/view", methods=['GET'])
def view_item():
    return render_template('item.html')
