from polls.models import Poll, Choice
from django.contrib import admin

# Stacked
# class ChoiceInline(admin.StackedInline):
# Tabular	
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3
	
class PollAdmin(admin.ModelAdmin):
	# apenas altera a ordem em que os atributos sao mostrados
	# fields = ['pub_date', 'question']
	# utilizando fieldsets e collapse
	fieldsets = [
		(None, {'fields' : ['question']}),
		('Date information', {'fields' : ['pub_date'], 'classes':['collapse']}),
	]
	# informa os campos que sao apresentados na tela de listagem das entidades
	list_display = ('question', 'pub_date', 'was_published_recently')
	# adicionar respostas
	inlines = [ChoiceInline]
	# adiciona capacidade de filtrar pela data
	list_filter = ['pub_date']
	# adiciona campo para buscas
	search_fields = ['question']
	# adiciona
	date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
