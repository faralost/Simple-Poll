from django.urls import path

from webapp.views.poll_views import index_view

urlpatterns = [
    path('', index_view, name='index'),
]
