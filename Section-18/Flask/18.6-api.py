from tkinter import NO
from flask import Flask, jsonify, request

app=Flask(__name__)

## Static data
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def home():
    return 'Welcome to sample todo list app'

## fetching all items: GET
@app.route('/items')
def getitems():
    return jsonify(items)

## fetch specific item: GET
@app.route('/item/<int:item_id>')
def getitem(item_id):
    item = next((item for item in items if item['id']==item_id), None)
    if item == None:
        return jsonify({'message':'No such item exists'})
    return jsonify(item)

## Create new task: Post
@app.route('/item', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'error':'insuficient data'})
    print(request.json)
    new_item = {
        'id':items[-1]['id'] +1 if items else 1,
        'name': request.json['name'],
        'description':request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

## update item: PUT
@app.route('/item/<int:update_id>', methods=['PUT'])
def update_item(update_id):
    item = next((item for item in items if item['id'] == update_id) ,None)
    if item is None:
        return jsonify({'error':'item does not exist/not found'})
    
    if not request.json or not 'name' in request.json or not 'description' in request.json:
        return jsonify({'error':'insuficient data'})

    for index, item in enumerate(items):
        if item['id'] == update_id:
            updated_item_index = index
            item['name'] = request.json['name']
            item['description'] = request.json['description']
   
    return jsonify(items[updated_item_index])

## delete item: DELETE
@app.route('/item/<int:delete_id>', methods=['DELETE'])
def delete_item(delete_id):
    items[:] = [item for item in items if item['id'] != delete_id]
    return jsonify({'message':'item deleted successfully'})

if __name__ == '__main__':
    app.run(port=2024, debug=True)