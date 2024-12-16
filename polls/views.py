from django.db.models import F

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404
from django.shortcuts import render

from django.urls import reverse

from django.views.generic import DetailView
from django.views.generic import ListView

from polls.models import Choice
from polls.models import Question


class PoolsListView(ListView):
    template_name = "polls/list.html"
    context_object_name = "latest_questions"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class PollsDetailView(DetailView):
    template_name = "polls/detail.html"
    model = Question


class PollsResultsView(DetailView):
    template_name = "polls/results.html"
    model = Question


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


def votes(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
