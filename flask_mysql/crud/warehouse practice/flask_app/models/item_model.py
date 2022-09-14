from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask import Flask
from flask_app import app
from flask_app.models import user_model
from flask_app.models import order_model

class Item:
    def __init__(self) -> None:
        pass