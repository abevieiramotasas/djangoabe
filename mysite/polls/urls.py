from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from polls.models import Poll


# separando o prefixo polls.views
# urlpatterns = patterns('polls.views',
#     url(r'^$', 'index'),
#     url(r'^(?P<poll_id>\d+)/$', 'detail'),
#     url(r'^(?P<poll_id>\d+)/results/$', 'results'),
#     url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
# )

# utilizando generic views
urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            # indica que a lista de poll retornada tera esse nome
            context_object_name='latest_poll_list',
            # default de template_name <app_name>/<model_name>_list.html
            template_name='polls/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            # default de template_name <app_name>/<model_name>_detail.html
            template_name='polls/detail.html')),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'),
        name='poll_results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)
