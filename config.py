import os

class Config:
    # Flask 기본 설정
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')

    # SQLAlchemy 데이터베이스 URI 설정 (MySQL 예시)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'
    
    # SQLAlchemy 추가 설정
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 성능 최적화를 위해 비활성화

config = Config()