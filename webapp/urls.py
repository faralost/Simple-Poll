from django.urls import path

from webapp.views.choice_views import PollChoiceAddView, PollChoiceUpdate, PollChoiceDelete
from webapp.views.poll_views import PollsIndexView, PollDetailView, PollAddView, PollUpdateView, PollDeleteView

urlpatterns = [
    path('', PollsIndexView.as_view(), name='index'),
    path('poll/<int:pk>/', PollDetailView.as_view(), name='poll_detail_view'),
    path('polls/add/', PollAddView.as_view(), name='poll_add'),
    path('poll/<int:pk>/update/', PollUpdateView.as_view(), name='poll_update'),
    path('poll/<int:pk>/delete/', PollDeleteView.as_view(), name='poll_delete'),
    path('poll/<int:pk>/choices/add/', PollChoiceAddView.as_view(), name='poll_choice_add'),
    path('choice/<int:pk>/update/', PollChoiceUpdate.as_view(), name='poll_choice_update'),
    path('choice/<int:pk>/delete/', PollChoiceDelete.as_view(), name='poll_choice_delete'),
]
