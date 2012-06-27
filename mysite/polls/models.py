from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# modelos devem estender models.Model
class Poll(models.Model):
	# campos do tipo charfield requerem que max_length seja definido
    question = models.CharField(max_length=200)
    # pode-se passar como primeiro parametro do campo um nome para ser utilizado quando necessario
    # um nome human-readable para o campo
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
    	return self.question
    def was_published_recently(self):
    	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	# usando chave estrangeira/ relacionamento
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
    	return self.choice