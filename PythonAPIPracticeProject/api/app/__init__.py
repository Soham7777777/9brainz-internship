import tomllib
from flask import Flask, Response, jsonify, make_response
import click
import os
from flask.cli import FlaskGroup
import sys
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from pydantic import JsonValue
from app.pydantic_models import APIErrorResponseModel, APISuccessResponseModel, ResponseModel
from werkzeug import exceptions


class InvalidAPIResponseFormatError(Exception):
    def __init__(self, message: str, error_code: int | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.error_code = error_code
    
    def __str__(self) -> str:
        if self.error_code:
            return f"{self.message} (Error Code: {self.error_code})"
        return self.message


def make_success_response(data: JsonValue) -> Response:
    return make_response(jsonify(ResponseModel(response=data).model_dump(mode='json')), 200)


title = '''
                           
                           
     █████╗ ██████╗ ██████╗      ██████╗██╗     ██╗
    ██╔══██╗██╔══██╗██╔══██╗    ██╔════╝██║     ██║
    ███████║██████╔╝██████╔╝    ██║     ██║     ██║
    ██╔══██║██╔═══╝ ██╔═══╝     ██║     ██║     ██║
    ██║  ██║██║     ██║         ╚██████╗███████╗██║
    ╚═╝  ╚═╝╚═╝     ╚═╝          ╚═════╝╚══════╝╚═╝
                                                   

'''


db = SQLAlchemy()
jwt = JWTManager()


@jwt.expired_token_loader
def expired_token_callback(jwt_header: dict[str, str], jwt_payload: dict[str, str]) -> Response:
    raise exceptions.BadRequest("The token can no longer be used")


@jwt.invalid_token_loader
def invalid_token_callback(reason: str) -> Response:
    raise exceptions.BadRequest(reason)


def ensure_configuration_availability(instance_path: str) -> str:
    if not os.path.exists(instance_path):
        try:
            os.makedirs(instance_path)
        except Exception as e:
            click.echo(click.style(f"Cannot create instance directory.\n{str(e)}", fg='red', bold=True))
            sys.exit()
    profile = os.getenv('PROFILE', 'Deployment')
    abs_config_path = os.path.join(instance_path, profile+'.toml')
    if not os.path.exists(abs_config_path):
        click.echo(click.style(f"The configuration file '{profile}.toml' is missing at {instance_path}.", fg='red', bold=True), nl=False)
        click.echo(click.style("Provide explicit configuration file to run application.", underline=True, fg='red', bold=True))
        sys.exit()
    return profile+'.toml'


def make_app() -> Flask:
    application = Flask(__name__, instance_relative_config=True)
    config_file = ensure_configuration_availability(application.instance_path)
    application.config.from_file(config_file, load=tomllib.load, text=False)
    
    from app import errorhandlers as errhndl
    application.register_error_handler(exceptions.HTTPException, errhndl.jsonify_errors)
    
    jwt.init_app(application)
    db.init_app(application)
    with application.app_context():
        db.reflect()

    from .blueprints import user, admin
    application.register_blueprint(user.bp)
    application.register_blueprint(admin.bp)


    @application.get('/')
    def home() -> Response:
        return make_success_response(dict(any="This is the format of success response"))


    @application.after_request
    def validate_succes_response(response: Response) -> Response:
        model = ResponseModel.model_validate_json([*response.response][0])
        if response.status_code != 200:
            if type(model.response) != str:
                raise  InvalidAPIResponseFormatError("The Success API Response is not a valid str")

            return make_response(jsonify(APIErrorResponseModel(message=model.response).model_dump(mode='json')), 200)

        if type(model.response) == str:
            raise  InvalidAPIResponseFormatError("The Success API Response is not a valid JsonValue")
              
        return make_response(jsonify(APISuccessResponseModel(data=model.response).model_dump(mode='json')))


    click.echo(click.style(title, fg='green'))
    return application


@click.group(cls=FlaskGroup, create_app=make_app)
def cli() -> None:
    """The CLI to interact with this application."""
