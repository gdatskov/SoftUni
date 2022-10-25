from django.db import models

# Map to a DB table
class Task(models.Model):
    # varchar(30)
    name = models.CharField(
        max_length=30,
        null=False,
    )
    description = models.TextField()
    priority = models.IntegerField()

