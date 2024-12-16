from django.views.generic import DetailView as BaseView

from polls.models import Question


class DetailView(BaseView):
    template_name = "polls/detail.html"
    model = Question
