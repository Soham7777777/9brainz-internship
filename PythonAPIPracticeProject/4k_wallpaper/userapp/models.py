from typing import Any
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager): # type: ignore

    def create_user(self, email: str, password: str | None = None) -> Any:
        if not email:
            raise ValueError("The Email must be set")
        if not password:
            raise ValueError("The Password must be set")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email: str, password: str | None = None) -> Any:
        return self.create_user(email, password)


class User(AbstractBaseUser):
    email = models.EmailField("email address", unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    objects = UserManager()
