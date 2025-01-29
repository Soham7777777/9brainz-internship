from functools import wraps
from flask import current_app, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug import exceptions
from app.sqlalchemy_models import User


def login_required(): # type: ignore
    def decorator(view): # type: ignore
        @jwt_required()
        @wraps(view)
        def wrapped_view(**kwargs): # type: ignore
            user: User = User.query.get(int(get_jwt_identity()))
            if user is not None:
                if current_app.config["LOGIN_TYPE"] == "single":
                    device_type = request.args["device_type"]
                    if user.device_type == device_type:
                        return view(user, **kwargs)
                    raise exceptions.BadRequest("You are logged out from this device")
                return view(user, **kwargs)
            raise exceptions.BadRequest("User not found")
        return wrapped_view
    return decorator
