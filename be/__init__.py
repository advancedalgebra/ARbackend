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

    application.register_blueprint(auth.bp, url_prefix='/ar/api/auth')
    application.register_blueprint(location.bp, url_prefix='/ar/api/location')

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
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    range = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(400), nullable=False)

    def __init__(self, latitude, longitude, range, name, description):
        self.name = name
        self.range = range
        self.description = description
        self.latitude = latitude
        self.longitude = longitude


class Event(db.Model):
    __tablename__ = 'Event'
    event_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    building_id = db.Column(db.String(40), nullable=False)
    user_id = db.Column(db.String(40), nullable=False)
    title = db.Column(db.String(40), nullable=False)
    content = db.Column(db.String(400), nullable=False)
    time = db.Column(db.String(40), nullable=False)

    def __init__(self, building_id, user_id, title, content, time):
        self.user_id = user_id
        self.building_id = building_id
        self.title = title
        self.content = content
        self.time = time