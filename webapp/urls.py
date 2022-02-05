from django.urls import path

from webapp.views.poll_views import PollsIndexView, PollDetailView

urlpatterns = [
    path('', PollsIndexView.as_view(), name='index'),
    path('poll/<int:pk>/', PollDetailView.as_view(), name='poll_detail_view'),
]
