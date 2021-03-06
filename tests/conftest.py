import pytest, os
from modules.db_model import db
from flask import Flask
from modules import factory
@pytest.fixture
def app():
    app = factory.create_app("hungry-girlfriend-test", "development")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['TESTING'] = True
    yield app
