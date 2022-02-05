from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PollForm
from webapp.models import Poll


class PollsIndexView(ListView):
    template_name = 'poll/index.html'
    model = Poll
    ordering = ['-created_at']
    paginate_by = 7


class PollDetailView(DetailView):
    template_name = 'poll/detail.html'
    model = Poll


class PollAddView(CreateView):
    template_name = 'poll/create.html'
    form_class = PollForm
    model = Poll


class PollUpdateView(UpdateView):
    template_name = 'poll/update.html'
    form_class = PollForm
    model = Poll


class PollDeleteView(DeleteView):
    template_name = 'poll/delete.html'
    model = Poll
    success_url = reverse_lazy('index')
