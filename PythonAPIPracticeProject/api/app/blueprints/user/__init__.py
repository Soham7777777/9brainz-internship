from flask import Blueprint, current_app, request
from flask_jwt_extended import create_access_token
from werkzeug import exceptions, Response
from app.pydantic_models import UserModel
from app.sqlalchemy_models import User
from app import db, make_success_response
from app.decorators import login_required


bp = Blueprint(
    'User',
    __name__,
    url_prefix='/user',
    static_folder='static',
    template_folder='templates'
)


@bp.get('/login')
def login() -> Response:
    name = request.args["name"]
    password_text = request.args["password_text"]

    user = User.query.filter_by(name=name, password_text=password_text).one_or_none()

    if user is not None:
        data=dict(token=create_access_token(identity=str(user.id)))
        if current_app.config["LOGIN_TYPE"] == "single":
            device_type = request.args["device_type"]
            user.device_type = device_type
            db.session.commit()
            data["message"] = f"You are being logged out of every devices other than your current device - {device_type}"
        return make_success_response(data=data)

    raise exceptions.Unauthorized()


@bp.get('/protected')
@login_required() # type: ignore
def protected(user: User) -> Response:
    return make_success_response(data=UserModel.model_validate(user).model_dump(mode='json'))
