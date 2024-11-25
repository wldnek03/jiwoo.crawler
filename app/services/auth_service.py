from flask_jwt_extended import create_access_token, decode_token
from datetime import timedelta

def generate_token(username):
    """
    사용자 이름을 기반으로 JWT 토큰 생성
    """
    access_token = create_access_token(identity=username, expires_delta=timedelta(hours=1))
    return access_token

def verify_token(token):
    """
    JWT 토큰 검증
    """
    try:
        decoded = decode_token(token)
        return decoded['identity']
    except Exception as e:
        return None