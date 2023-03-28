from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email: str, password: str, **extra_fields) -> Any:
        if not email:
            raise ValueError("Missing e-mail")
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password=None, **extra_fields) -> Any:
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields) -> Any:
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        if not extra_fields.get("is_superuser"):
            raise ValueError("Super user must be true")
        if not extra_fields.get("is_staff"):
            raise ValueError("Staff user must be true")
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField("E-mail", unique=True)
    is_staff = models.BooleanField("Staff", default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self) -> str:
        return str(self.email)

    objects = UserManager()
