from django.db.models import F
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404
from django.shortcuts import render

from django.urls import reverse

from polls.models import Choice
from polls.models import Question


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
