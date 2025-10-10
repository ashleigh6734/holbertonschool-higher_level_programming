from flask import Flask
from flask import jsonify

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route('/data/<username>')
def get_user(username):
    if username in users:
        return jsonify({username: users[username]})
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route('add_user', methods=['POST'])
def add_user():
    from flask import request
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    if username and email:
        users[username] = email
        return jsonify({"message": "User added successfully"}), 201
    else:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__": app.run()
