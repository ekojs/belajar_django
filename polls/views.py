from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Question


def index(request):
    latest_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_list': latest_list,}
    return render(request, 'polls/index.html', context)

def detail(request, q_id):
    q = get_object_or_404(Question, pk=q_id)
    return render(request, 'polls/detail.html', {'q': q})

def results(request, q_id):
    q = get_object_or_404(Question, pk=q_id)
    return render(request, 'polls/results.html', {'q': q})

def vote(request, q_id):
    q = get_object_or_404(Question, pk=q_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['c'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'q':q,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(q_id,)))
