from django.http import HttpResponse
from django.http import Http404

from django.shortcuts import render

from polls.models import Question


import pdb

def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_questions": latest_questions,
    }
    return render(request=request, template_name="polls/index.html", context=context)


def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")

    context = {
        "question": question
    }
    return render(request=request, template_name="polls/detail.html", context=context)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def votes(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
