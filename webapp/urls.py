from django.urls import path

from webapp.views.poll_views import PollsIndexView

urlpatterns = [
    path('', PollsIndexView.as_view(), name='index'),
]
