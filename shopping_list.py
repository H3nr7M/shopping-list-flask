#Importing the Flask class from the flask module
from flask import Flask, jsonify, request
#Creating an instance of the Flask class
app = Flask(__name__)

# a list to store the shopping items the first time the app is run
shopping_list = ['milk', 'bread', 'eggs']

# endpoint to add an item to the shopping list
@app.route('/shopping_list', methods=['POST'])
def add_item():
    item = request.json.get('item')
    shopping_list.append(item)
    # if the item is successfully added to the shopping list, return a message, else return an error message
    return jsonify({'message': 'Item added to shopping list.'}), 201

# endpoint to get the shopping list
@app.route('/shopping_list', methods=['GET'])
def get_shopping_list():
    return jsonify({'shopping_list': shopping_list}), 200

# If this file is run directly, run the app
if __name__ == '__main__':
    app.run(debug=True)
