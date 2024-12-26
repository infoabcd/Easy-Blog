from datetime import datetime
from sqlalchemy import or_
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

# 用户类
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    @staticmethod
    def create_user(username, password):
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()

# 文章类
class Content(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(500), nullable=False)
    images = db.Column(db.String(200), nullable=True)
    posttime = db.Column(db.DateTime, default=datetime.now)

# 数据库初始化(创建数据库和表And结构)
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


        # 插入默认用户 - 测试
        if not User.query.filter_by(username='admin').first():
            User.create_user('admin', '123456')
