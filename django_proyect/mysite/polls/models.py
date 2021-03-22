from django.db import models
import datetime
from django.utils import timezone
import ipdb;
# Create your models here.

class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        now = timezone.now()
        ipdb.set_trace()
        return now - datetime.timedelta(days=1) <= self.publish_date <= now

class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

