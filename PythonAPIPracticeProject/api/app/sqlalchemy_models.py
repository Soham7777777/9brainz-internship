from app import db
from sqlalchemy import orm

class User(db.Model): # type: ignore
    __table__ = db.metadata.tables["users"]
    id: orm.Mapped[int]
    name: orm.Mapped[str]
    password_text: orm.Mapped[str]
    device_type: orm.Mapped[str]
    remember_token: orm.Mapped[str]
