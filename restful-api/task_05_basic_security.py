#!/usr/bin/env python3
"""
Task 05: Basic Security
Implement Basic and JWT authentication for the Flask API.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
# A long, random, and secret key is crucial for JWT security.
# In a real app, this should be loaded from environment variables.
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY', 'super-secret-key')

jwt = JWTManager(app)
auth = HTTPBasicAuth()

# In-memory user data store
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# --- Custom Error Handlers for JWT ---
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

# --- Basic Authentication ---

@auth.verify_password
def verify_password(username, password):
    """Verify user credentials for Basic Authentication."""
    if username in users and check_password_hash(users.get(username)['password'], password):
        return users.get(username)
    return None

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """An endpoint protected by Basic Authentication."""
    return jsonify({"message": "Basic Auth: Access Granted"})

# --- JWT Authentication ---

@app.route("/login", methods=["POST"])
def login():
    """Login a user and return a JWT access token."""
    data = request.get_json()
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Missing username or password"}), 400

    username = data["username"]
    password = data["password"]

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        # Create token with user's role in the claims
        additional_claims = {"role": user["role"]}
        access_token = create_access_token(identity=username, additional_claims=additional_claims)
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """An endpoint protected by JWT."""
    current_user = get_jwt_identity()
    return jsonify(message="JWT Auth: Access Granted", user=current_user)

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """An endpoint protected by JWT and restricted to admins."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    
    current_user = get_jwt_identity()
    return jsonify(message="Admin Access: Granted", admin=current_user)

# Main execution block
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)