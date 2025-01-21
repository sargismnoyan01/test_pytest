from django.db import models


class UserClass(models.Model):
    name = models.CharField('name',max_length=255)
    surname = models.CharField('surname',max_length=255)