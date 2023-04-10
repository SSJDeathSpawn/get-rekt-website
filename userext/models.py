from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def save_user(self, regno, password, **extra_fields):
        if not regno:
            raise ValueError("The given regno must be set")

        user = self.model(regno=regno, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, regno, password, **extra_fields):
        extra_fields["is_superuser"] = False
        extra_fields["is_staff"] = False

        return self.save_user(regno, password, **extra_fields)

    def create_superuser(self, regno, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser should be True")

        extra_fields["is_staff"] = True

        return self.save_user(regno, password, **extra_fields)


class UserEXT(AbstractBaseUser, PermissionsMixin):
    regno = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=200)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "regno"

    objects = UserManager()

    def firstname(self):
        return self.name.split()[0]


# Create your models here.
