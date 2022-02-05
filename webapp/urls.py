from django.urls import path

from webapp.views.poll_views import PollsIndexView, PollDetailView, PollAddView, PollUpdateView

urlpatterns = [
    path('', PollsIndexView.as_view(), name='index'),
    path('poll/<int:pk>/', PollDetailView.as_view(), name='poll_detail_view'),
    path('polls/add/', PollAddView.as_view(), name='poll_add'),
    path('poll/<int:pk>/update/', PollUpdateView.as_view(), name='poll_update'),
]
