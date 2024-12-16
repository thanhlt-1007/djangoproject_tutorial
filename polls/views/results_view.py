from django.views.generic import DetailView as BaseView

from polls.models import Question


class ResultsView(BaseView):
    template_name = "polls/results.html"
    model = Question
