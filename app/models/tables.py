from datetime import datetime
from operator import delitem
from app import db, lm
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@lm.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name: str, email: str, password: str) -> None:
        self.password = generate_password_hash(password, method='sha256')
        self.name = name
        self.email = email

    def verify_password( user_password: str = None, form_password: str = None) -> None:
        print(user_password, form_password)
        return check_password_hash(user_password, form_password)
    
    def __repr__(self):
        return f'<User {self.name}'

class Category( db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name: str, description: str = '') -> None:
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<User {self.name}'

class Type( db.Model):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
    
    def __repr__(self):
        return f'<User {self.name}'

class Income( db.Model):
    __tablename__ = 'incomes'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    value = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    category = db.relationship('Category', foreign_keys=category_id)

    def __init__(self, name: str, description: str, value: str, date: datetime, category_id: int = None) -> None:
        self.name = name
        self.description = description
        self.value = value
        self.date = date
        self.category_id = category_id
    
    def __repr__(self):
        return f'<User {self.name}'

class Expense( db.Model):
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    value = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    category = db.relationship('Category', foreign_keys=category_id)
    type = db.relationship('Type', foreign_keys=type_id)

    def __init__(self, name: str, description: str, value: str, date: datetime, type: int, category_id: int = None) -> None:
        self.name = name
        self.description = description
        self.value = value
        self.date = date
        self.category_id = category_id
        self.type = type
    
    def __repr__(self):
        return f'<User {self.name}'

