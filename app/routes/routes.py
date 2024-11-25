from flask import Blueprint, jsonify, request
import jwt
import bcrypt
from app import db

bp = Blueprint('routes', __name__)

SECRET_KEY = 'Jiwoo123'  # JWT 시크릿 키

# 회원가입 API
@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        with db.engine.connect() as conn:
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            conn.execute(sql, (username, email, hashed_password))
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# 로그인 API
@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        with db.engine.connect() as conn:
            sql = "SELECT id, password FROM users WHERE username=%s"
            result = conn.execute(sql, (username,))
            user = result.fetchone()

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            # JWT 토큰 생성
            token = jwt.encode({'user_id': user['id']}, SECRET_KEY, algorithm='HS256')
            return jsonify({"token": token}), 200
        else:
            return jsonify({"error": "Invalid username or password"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@bp.route('/jobs', methods=['GET'])
def get_jobs():
    # 샘플 데이터 반환
    return jsonify({"jobs": [
        {"title": "Backend Developer", "company": "ABC Corp", "location": "Seoul"},
        {"title": "Frontend Developer", "company": "XYZ Inc", "location": "Busan"}
    ]})

@bp.route('/protected', methods=['GET'])
def protected_route():
    return jsonify({"message": "This is a protected route"})


