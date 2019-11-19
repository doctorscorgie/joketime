from django.db import models


class JokeType(models.Model):
    type = models.CharField(max_length=20)
    description = models.TextField()
    def __str__(self):
        return self.type


class Joke(models.Model):
    joketype = models.ForeignKey('JokeType', on_delete=models.CASCADE)
    text = models.TextField()
    source = models.CharField(max_length=50)
    def __str__(self):
        return self.text