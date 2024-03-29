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
    # informa como o campo representado pelo metodo was_published_recently deve ser apresentado
    # qual atributo deve ser utilizado para ordena-lo
    was_published_recently.admin_order_field = 'pub_date'
    # informa que o campo eh booleano(fica um negocio verde bonito)
    was_published_recently.boolean = True
    # informa como o campo eh descrito(default eh o nome do metodo sem os _ )
    was_published_recently.short_description = "Published recently?"

class Choice(models.Model):
	# usando chave estrangeira/ relacionamento
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
    	return self.choice
