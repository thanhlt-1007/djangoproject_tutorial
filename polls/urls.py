from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.PoolsListView.as_view(), name="list"),
    path("<int:pk>", views.PollsDetailViiew.as_view(), name="detail"),
    path("<int:question_id>/results", views.results, name="results"),
    path("<int:question_id>/votes", views.results, name="votes"),
    path("<int:question_id>/vote", views.vote, name="vote"),
]
