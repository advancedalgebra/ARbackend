from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    application = Flask(__name__)
    application.config.from_mapping(
        SQLALCHEMY_DATABASE_URI='mysql://root:root@120.79.19.172/ARbackend',
        SQLALCHEMY_TRACK_MODIFICATIONS='False'
    )
    db.init_app(application)

    @application.route('/hello')
    def hello():
        db.create_all()
        return 'Hello, World!'

    from be.view import auth
    from be.view import location
    from be.view import init_db

    application.register_blueprint(auth.bp, url_prefix='/ar/api/auth')
    application.register_blueprint(location.bp, url_prefix='/ar/api/location')
    application.register_blueprint(init_db.bp, url_prefix='/init')

    return application


class User(db.Model):
    __tablename__ = 'User'
    username = db.Column(db.String(40), unique=True, primary_key=True)
    password = db.Column(db.String(400), nullable=False)
    token = db.Column(db.String(1000), nullable=True)

    def __init__(self, username, password, token=None):
        self.username = username
        self.password = password
        self.token = token


class Building(db.Model):
    __tablename__ = 'Building'
    building_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    latitude_upper = db.Column(db.Float, nullable=False)
    longitude_upper = db.Column(db.Float, nullable=False)
    latitude_lower = db.Column(db.Float, nullable=False)
    longitude_lower = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    def __init__(self, latitude_upper, longitude_upper, latitude_lower, longitude_lower, name, description):
        self.name = name
        self.latitude_upper = latitude_upper
        self.description = description
        self.latitude_lower = latitude_lower
        self.longitude_lower = longitude_lower
        self.longitude_upper = longitude_upper


class Event(db.Model):
    __tablename__ = 'Event'
    event_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    building_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(40), nullable=False)
    title = db.Column(db.String(40), nullable=False)
    content = db.Column(db.String(400), nullable=False)
    time = db.Column(db.String(40), nullable=False)

    def __init__(self, building_id, username, title, content, time):
        self.username = username
        self.building_id = building_id
        self.title = title
        self.content = content
        self.time = time
