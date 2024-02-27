from flask import Flask, request, jsonify

app = Flask(__name__)

users_data = [
    {
        'id': 0,
        'name': 'Pedro Macêdo',
        'city':  'Guarabira'
    },
    {
        'id': 1,
        'name': 'Luis Medeiros',
        'city':  'Itabaiana'
    },
    {
        'id': 2,
        'name': 'Rennyson Cavalcante',
        'city':  'Guarabira'
    },
    {
        'id': 3,
        'name': 'Jonatan',
        'city':  'Cuité'
    }
]

@app.route('/user/<name>', methods = ['GET','DELETE'])
def user(name):
    if request.method == 'GET':
        for i in range(len(users_data)):
            if users_data[i]['name'] == name: 
                print(name)
                return f'Hello, {name}! Welcome to TDG COMPANY.'
        return f'Hello, {name}! Access not authorized to TDG COMPANY.'

    if request.method == 'DELETE':
        for i in range(len(users_data)):
            if users_data[i]['name'] == name: 
                users_data.pop(i)
                return jsonify(users_data), 200
        return 'User not found', 204


@app.route('/user/', methods = ['POST'])
def create_user():
    Id = users_data[-1]['id']+1
    new_name = request.form['name']
    new_city = request.form['city']

    new_user = { 
        'id': Id,
        'name': new_name,
        'city': new_city 
    }
    users_data.append(new_user)
    return jsonify(users_data), 201

@app.route('/')
def index():
    return 'hello world'

if __name__ == "__main__":
    app.run()