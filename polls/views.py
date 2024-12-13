from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.db.models import F

from django.urls import reverse

from polls.models import Question
from polls.models import Choice

import pdb


def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_questions": latest_questions,
    }
    return render(request=request, template_name="polls/index.html", context=context)


def detail(request, question_id):
    question = get_object_or_404(klass=Question, id=question_id)
    context = {
        "question": question
    }
    return render(request=request, template_name="polls/detail.html", context=context)


def vote(request, question_id):
    question = get_object_or_404(klass=Question, id=question_id)
    try:
        choice = question.choice_set.get(id=request.POST["choice_id"])
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            "error_message": "You didn't select a choice."
        }
        return render(request=request, template_name="polls/detail.html", context=context)

    choice.votes = F("votes") + 1
    choice.save()

    redirect_url = reverse(viewname="polls:results", args=(question.id,))
    return HttpResponseRedirect(redirect_to=redirect_url)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def votes(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
