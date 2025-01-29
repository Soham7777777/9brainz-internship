from typing import Callable, Generator
from flask.testing import FlaskClient
import pytest
from app import make_app, db
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


@pytest.fixture
def app() -> Flask:
    load_dotenv("./.flaskenv")
    return make_app()


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture
def database(app: Flask) -> Generator[SQLAlchemy, None, None]:
    with app.app_context():
        yield db


@pytest.fixture
def build_url_for(app: Flask) -> Generator[Callable[[str], str], None, None]:
    with app.app_context():
        yield url_for


# @pytest.fixture
# def token(client) -> str:
#     res = client.get('User.login',json=dict(**valid_user))
#     token = res.json['token']
#     res = client.post('/auth/login',headers={"Authorization":f'Bearer {token}'}, json={'otp':'0000'})
#     return res.json['token']


# @pytest.fixture
# def user(app) -> User:
#     with app.app_context():
#         user = User(**valid_user)
#     return user


# {
#     "success": true,
#     "message": "Login Successfully.",
#     "data": {
#         "id": 3,
#         "username": "9B",
#         "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTkyLjE2OC4wLjE1NTo4MDgxL2FwaS91c2VyL2xvZ2luIiwiaWF0IjoxNzM3NjExMzM5LCJuYmYiOjE3Mzc2MTEzMzksImp0aSI6IjRUN2RrdnllQk11S21hNmEiLCJzdWIiOiIzIiwicHJ2IjoiZjY0ZDQ4YTZjZWM3YmRmYTdmYmY4OTk0NTRiNDg4YjNlNDYyNTIwYSJ9.PLtiyufEI0IbBqvu3BbTX7UwgCkfoq7Av2i66cvPasQ"
#     }
# }
