from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    CATEGORY_NAME_MAX_LEN = 15

    name = models.CharField(
        max_length=CATEGORY_NAME_MAX_LEN,
        unique=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT
    )

    def __str__(self):
        return self.name


class Todo(models.Model):
    TODO_TITLE_MAX_LEN = 30
    DEFAULT_STATE = False

    title = models.CharField(
        max_length=TODO_TITLE_MAX_LEN,
    )

    description = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.RESTRICT,
    )

    state = models.BooleanField(
        default=DEFAULT_STATE
    )

    def __str__(self):
        return self.title
