from django.views.generic import ListView

from webapp.models import Poll


class PollsIndexView(ListView):
    template_name = 'poll/index.html'
    model = Poll
