from flask import Flask,jsonify,request

app = Flask(__name__)
items = [
    {'id':1,'name':'Item1','description':'This is item 1'},
    {'id':2,'name':'Item2','description':'This is item 2'}
]

@app.route('/')
def home():
    return 'Welcome to the To Do List App'

@app.route('/items',methods = ['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>',methods = ['GET'])
def get_item_id(item_id):
    item = next((item for item in items if item_id == item['id']),None)
    if item is None:
        return jsonify({'error':'item not found'})
    return jsonify(item)

@app.route('/items',methods = ['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({'error':'item not found'})
    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'description':request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

@app.route('/items/<int:item_id>',methods = ['PUT'])
def update_item(item_id):

    item = next((item for item in items if item_id == item['id']),None)
    if item is None:
        return jsonify({'error':'item not found'})
    item['name'] = request.json.get('name',item['name'])
    item['description'] = request.json.get('description',item['description'])
    return jsonify(item)

@app.route('/items/<int:item_id>',methods = ['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item_id != item['id']]
    return jsonify(items)
if __name__ == '__main__':
    app.run(debug=True)