from flask import Blueprint, request, jsonify, session
from werkzeug.security import check_password_hash, generate_password_hash
from models import db, Login

login_routes = Blueprint('login_routes', __name__)

ADMIN_EMAIL = 'admin@example.com'
ADMIN_PASSWORD = 'admin123'

@login_routes.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
        session['role'] = 'admin'
        session['email'] = email
        return jsonify({"message": "Admin login successful", "role": "admin"}), 200

    user = Login.query.filter_by(email=email).first()

    if user:
        if check_password_hash(user.password, password):
            session['login_id'] = user.login_id
            session['role'] = user.role
            return jsonify({"message": "Customer login successful", "role": user.role}), 200
        else:
            return jsonify({"message": "Invalid password"}), 401

    hashed_password = generate_password_hash(password)
    new_user = Login(
        name=data.get('name', 'Guest'),
        email=email,
        password=hashed_password,
        phone_number=data.get('phone_number', ''),
        role='customer'
    )
    db.session.add(new_user)
    db.session.commit()

    session['login_id'] = new_user.login_id
    session['role'] = new_user.role

    return jsonify({"message": "New customer account created and logged in", "role": "customer"}), 201
