from django.views.generic import ListView, DetailView

from webapp.models import Poll


class PollsIndexView(ListView):
    template_name = 'poll/index.html'
    model = Poll
    ordering = ['-created_at']
    paginate_by = 7


class PollDetailView(DetailView):
    template_name = 'poll/detail.html'
    model = Poll

