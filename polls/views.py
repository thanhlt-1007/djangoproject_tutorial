from django.http import HttpResponse
from django.template import loader

from polls.models import Question


import pdb

def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_questions": latest_questions,
    }
    content = template.render(context=context, request=request)
    return HttpResponse(content)


def detail(request, question_id):
    return HttpResponse("You're looking at the question %s." % question_id)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def votes(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
