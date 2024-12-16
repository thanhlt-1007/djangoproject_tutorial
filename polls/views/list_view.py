from django.views.generic import ListView as BaseView

from polls.models import Question


class ListView(BaseView):
    template_name = "polls/list.html"
    context_object_name = "latest_questions"


    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
