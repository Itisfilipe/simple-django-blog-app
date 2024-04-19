from django.db import models

from users.models import Profile

# TODO: Create the tags model


class Post(models.Model):
    text = models.TextField(blank=True, null=True)

    # TODO: Add the tags app and m2m relationship
    # tags = ???
