from django.db import models
from django.contrib.auth.models import User


class Question_model(models.Model):
    question=models.TextField()
    answer=models.BooleanField()
    comment=models.TextField()

class Question_model2(models.Model):
    question=models.TextField()
    answer=models.BooleanField()
    comment=models.TextField()

class Question_model3(models.Model):
    question=models.TextField()
    answer=models.BooleanField()
    comment=models.TextField()

