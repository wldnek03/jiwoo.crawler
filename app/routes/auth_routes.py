from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'], email=data['email'])
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    user = User.query.filter_by(username=data['username']).first()
    
    if user and user.password == data['password']:  # 비밀번호는 실제로 해싱해야 함!
        return jsonify({"message": "Login successful!"}), 200
    
    return jsonify({"error": "Invalid credentials"}), 401