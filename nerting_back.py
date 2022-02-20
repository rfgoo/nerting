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


@app.route('/get', methods=['GET'])
def get_users():
    db = dataset.connect('sqlite:///nerting_db.db')
    user1 = []
    for user in db['User']:
        user1.append(user)
    return jsonify(user1)


@app.route('/get/<id>/', methods=['GET'])
def get_user(id):
    db = dataset.connect('sqlite:///nerting_db.db')
    return jsonify(db['User'].find_one(id=id))


if __name__ == "__main__":
    app.run(debug=True)
