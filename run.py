# app/__init__.py
from app import create_app
from flask import Flask
from app.routes import bp  # routes.py에서 Blueprint 가져오기

app = create_app()

if __name__ == '__main__':
    print("Starting Flask application...")  # 디버깅용 출력
    app.run(debug=True)

def create_app():
    app = Flask(__name__)
    
    # 설정 추가 (예: 데이터베이스, JWT 시크릿 키 등)
    app.config['SECRET_KEY'] = 'Jiwoo123'
    
    # Blueprint 등록
    app.register_blueprint(bp)

    return app
