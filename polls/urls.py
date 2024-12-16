from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.PoolsListView.as_view(), name="list"),
    path("<int:pk>", views.PollsDetailView.as_view(), name="detail"),
    path("<int:pk>/results", views.PollsResultsView.as_view(), name="results"),
    path("<int:question_id>/votes", views.votes, name="votes"),
    path("<int:question_id>/vote", views.vote, name="vote"),
]
