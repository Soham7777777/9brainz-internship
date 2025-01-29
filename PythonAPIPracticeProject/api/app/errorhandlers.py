from werkzeug import exceptions
from flask import Response, jsonify, make_response
from app.pydantic_models import ResponseModel


def jsonify_errors(e: exceptions.HTTPException) -> Response:
    message = e.description + ' ' if e.description is not None else '' + getattr(getattr(e, "original_exception", ''), "description", '')
    return make_response(jsonify(ResponseModel(response=message).model_dump(mode='json')), e.code)
