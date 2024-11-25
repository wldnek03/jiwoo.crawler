from flask import Flask
from app.db import db  # 분리된 db 객체 가져오기
from app.routes import bp

def create_app():
    app = Flask(__name__)
    
    # 앱 설정 추가
    app.config['SECRET_KEY'] = 'Jiwoo123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Jiwoo123@localhost/job_portal'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # SQLAlchemy 초기화
    db.init_app(app)

    # Blueprint 등록
    app.register_blueprint(bp)

    return app