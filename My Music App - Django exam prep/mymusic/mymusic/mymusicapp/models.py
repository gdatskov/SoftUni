from django.core import validators, exceptions
from django.db import models


def validate_string_is_alphanumeric(value):
    for char in value:
        if not char.isalnum() and char != "_":
            raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    MIN_USER_CHAR_LEN = 2
    MAX_USER_CHAR_LEN = 15

    username = models.CharField(
        max_length=MAX_USER_CHAR_LEN,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(2),
            validate_string_is_alphanumeric,
        ],
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return (self.username)



class Album(models.Model):
    MAX_LEN_ALBUM_NAME = 30
    MAX_LEN_ARTIST_NAME = 30
    MAX_LEN_GENRE_NAME = 30
    ALLOWED_GENRES = [
        "Pop Music",
        "Jazz Music",
        "R&B Music",
        "Rock Music",
        "Country Music",
        "Dance Music",
        "Hip Hop Music",
        "Other"
    ]

    album_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_ALBUM_NAME,
        unique=True,
    )
    artist = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_ARTIST_NAME,
    )
    genre = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_GENRE_NAME,
        choices=[(x, x) for x in ALLOWED_GENRES]
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            validators.MinValueValidator(0.0)
        ]
    )

