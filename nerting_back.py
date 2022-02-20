import dataset

from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/add', methods=['POST'])
def add_users():
    name = request.json['name']
    passwd = request.json['passwd']
    try:
        db = dataset.connect('sqlite:///nerting_db.db')
        db['User'].insert(dict(name=name, passwd=passwd))
        status = "200 OK"
    except:
        status = "ERROR"
    return jsonify({'name': name,
                    "Sattus": status})


@app.route('/get_all', methods=['GET'])
def get_users():
    db = dataset.connect('sqlite:///nerting_db.db')
    user1 = []
    for user in db['User']:
        user1.append(user)
    return jsonify(user1)


@app.route('/get_id/<id>/', methods=['GET'])
def get_user(id):
    db = dataset.connect('sqlite:///nerting_db.db')
    return jsonify(db['User'].find_one(id=id))


@app.route('/get_name/<name>/', methods=['GET'])
def get_user_name(name):
    db = dataset.connect('sqlite:///nerting_db.db')
    return jsonify(db['User'].find_one(name=name))

@app.route('/update/<id>/', methods=['PUT'])
def update_user(id):
    print(request.json['name'])
    print(request.json['passwd'])

    db = dataset.connect('sqlite:///nerting_db.db')
    db['User'].update(dict(id=id,
                           name=request.json['name'],
                           passwd=request.json['passwd']), ['id'])

    return get_user(id)


if __name__ == "__main__":
    app.run(debug=True)
