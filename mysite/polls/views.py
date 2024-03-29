# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from polls.models import Poll, Choice
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

# nao necessario por estarmos usando generic view
def index(request):
	# wadafuck, ta pegando tudo do bd e so entao limitando?! do tutorial do site...
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	# jeito feio
	# t = loader.get_template('polls/index.html')
	# c = Context({'latest_poll_list' : latest_poll_list})
	# output = ', '.join([p.question for p in latest_poll_list])	
	# return HttpResponse(t.render(c))
	return render_to_response('polls/index.html', {'latest_poll_list' : latest_poll_list })
	
# nao necessario por estarmos usando generic view
def detail(request, poll_id):
	# sem nan
    # try:
    #     p = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #     raise Http404
    # conan
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p}, context_instance=RequestContext(request))

# nao necessario por estarmos usando generic view	
def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p})
	
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # reverse retorna a url mapeada no urls.py com os parametros informados
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
	
