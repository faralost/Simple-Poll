from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from webapp.forms import PollForm, ChoiceForm
from webapp.models import Poll


class PollsIndexView(ListView):
    template_name = 'poll/index.html'
    model = Poll
    ordering = ['-created_at']
    paginate_by = 5


class PollDetailView(FormMixin, DetailView):
    template_name = 'poll/detail.html'
    model = Poll
    form_class = ChoiceForm

    def get_context_data(self, **kwargs):
        context = super(PollDetailView, self).get_context_data(**kwargs)
        poll_choices = self.object.choices.all()
        context['poll_choices'] = poll_choices
        return context


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
