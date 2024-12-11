from django.http import HttpResponse

from .models import Question


def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    question_texts = [question.question_text for question in latest_questions]
    content = ", ".join(question_texts)
    return HttpResponse(content)


def detail(request, question_id):
    return HttpResponse("You're looking at the question %s." % question_id)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def votes(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
