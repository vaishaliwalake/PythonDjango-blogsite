from django.db import models
from django.db.models import ForeignKey
from django.utils import timezone


class Question (models.Model):
    question_text = models.CharField (max_length=200)
    pub_date = models.DateTimeField ('date published')


class Choice (models.Model):
    question = models.ForeignKey (Question, on_delete=models.CASCADE)
    choice_text = models.CharField (max_length=200)
    votes = models.IntegerField (default=0)



def publish(self):
    self.published_date = timezone.now ()
    self.save ()

def _str__(self):
    return self.title
