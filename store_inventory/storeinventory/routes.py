"""
Store Inventory routes.
"""
from flask import flash, render_template, redirect, request, url_for
import requests

from storeinventory import app
from storeinventory.forms import ItemInformationForm


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


@app.route("/edit/<item_id>", methods=['GET', 'POST'])
def edit_item(item_id):

    get_item = requests.get("http://127.0.0.1:7776/get", data={'id': item_id})
    item = get_item.json()

    form = ItemInformationForm()

    if form.validate_on_submit():
        item_dump = {
            'id': item['id'],
            'name': form.item_name.data,
            'price': form.item_price.data,
            'quantity': form.item_quantity.data
        }

        requests.post('http://127.0.0.1:7776/update', data=item_dump)

        flash('Item info updated.', 'success')

        return redirect(url_for('home'))


    form.item_name.data = item['name']
    form.item_price.data = item['price']
    form.item_quantity.data = item['quantity']

    return render_template('edit.html', title='Edit Item', form=form)


@app.route("/add", methods=['GET', 'POST'])
def add_item():
    form = ItemInformationForm()

    if form.validate_on_submit():
        item_dump = {
            'name': form.item_name.data,
            'price': form.item_price.data,
            'quantity': form.item_quantity.data
        }

        requests.post('http://127.0.0.1:7776/new', data=item_dump)

        flash('New item added to inventory.', 'success')

        return redirect(url_for('home'))

    return render_template('add.html', title='Add Item', form=form)


@app.route("/view", methods=['GET'])
def view_item():
    return render_template('item.html')
