#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)


users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def usernames(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return users.get(username)


@app.post("/add_user")
def add_user():
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data["username"]
    users[username] = data
    return jsonify({"message": f"User added", "user": data}), 201


if __name__ == "__main__": app.run()
