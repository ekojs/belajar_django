from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_list': latest_list,}
    return render(request, 'polls/index.html', context)

def detail(request, q_id):
    q = get_object_or_404(Question, pk=q_id)
    return render(request, 'polls/detail.html', {'q': q})

def results(request, q_id):
    res = "You're looking at the results of question %s."
    return HttpResponse(res % q_id)

def vote(request, q_id):
    return HttpResponse("You're voting on question %s." % q_id)
