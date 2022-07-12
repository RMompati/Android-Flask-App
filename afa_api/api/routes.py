"""
Our API routes.
"""

from flask import request
import json

from api import app, db
from api.models import Item


@app.route('/', methods=['GET'])
def get_data():
    """
    Gets all the store inventory data.
    """

    items = Item.query.all()
    items_dump = []

    for item in items:
        items_dump.append({
            'id': item.id,
            'name': item.name,
            'price': item.price,
            'quantity': item.quantity
        })

    return json.dumps(items_dump)


@app.route('/new', methods=['GET', 'POST'])
def add_data():
    """
    Adds a new item to the store inventory data.
    """
    form = request.form

    if form['name']:
        item = Item(name=form['name'], price=form['price'], quantity=form['quantity'])
        db.session.add(item)
        db.session.commit()

    return "<h1>Adds New Data</h1>"


@app.route('/update', methods=['GET', 'POST'])
def edit_data():
    """
    Edits the store inventory data.
    """
    return "<h1>Edits Data</h1>"


@app.route('/delete', methods=['GET', 'POST'])
def delete_data():
    """
    Deletes an item from the store inventory data.
    """
    return "<h1>Deletes Data</h1>"
