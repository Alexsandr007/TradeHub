from products import models as pm
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.contrib.auth.validators import UnicodeUsernameValidator


SEX_CHOICES = (
    ('Мужчина', 'man'),
    ('Женщина', 'women')
)


SELLER_CHOICES = (
    ('Частное лицо', 'private_person'),
    ('Компания', 'company')
)


def user_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        "username",
        max_length=20,
        unique=True,
        help_text="Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    email = models.EmailField(max_length=50, null=True)
    number = models.CharField(max_length=20, null=True)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES)
    img = models.ImageField(upload_to=user_directory_path, height_field=100, width_field=100)
    date_of_birth = models.DateTimeField(null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    products = models.ForeignKey(pm.Products, on_delete=models.CASCADE)
    seller = models.CharField(max_length=20, choices=SELLER_CHOICES)
    exchange = models.BooleanField(default=False)
    objects = UserManager()

    EMAIL_FIELD = False
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'


class Reviews(models.Model):
    user_whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_whom')
    user_who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_who')
    value = models.IntegerField()

    class Meta:
        db_table = 'reviews'
