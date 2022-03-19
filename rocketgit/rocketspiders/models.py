from django.db import models


class Dataspider(models.Model):
    author = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=400)
    url = models.CharField(max_length=100)
    stars = models.CharField(max_length=30)
    forks = models.CharField(max_length=20)
    watching = models.CharField(max_length=30)
    commit = models.CharField(max_length=30)
    last_commit = models.CharField(max_length=400)
    release = models.CharField(max_length=100)
    last_release = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.author} - {self.name}"
