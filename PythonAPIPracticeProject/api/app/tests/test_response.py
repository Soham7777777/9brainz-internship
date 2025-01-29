from flask import url_for
from flask.testing import FlaskClient
from app.pydantic_models import APIErrorResponseModel, APISuccessResponseModel


def test_success_response_structure(client: FlaskClient) -> None:
    response = client.get('/')
    data = response.get_json()
    assert data is not None
    assert response.status_code == 200
    assert data["success"] == True
    APISuccessResponseModel.model_validate(data)


def test_error_response_structure(client: FlaskClient) -> None:
    response = client.get('/unknown_route')
    data = response.get_json()
    assert data is not None
    assert response.status_code == 200
    assert data["success"] == False
    APIErrorResponseModel.model_validate(data)