from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ChoiceForm
from webapp.models import Choice, Poll


class PollChoiceAddView(CreateView):
    form_class = ChoiceForm
    template_name = 'choice/create.html'
    model = Choice

    def form_valid(self, form):
        question = get_object_or_404(Poll, pk=self.kwargs.get("pk"))
        form.instance.question = question
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("poll_detail_view", kwargs={"pk": self.object.question.pk})


class PollChoiceUpdate(UpdateView):
    form_class = ChoiceForm
    template_name = 'choice/update.html'
    model = Choice

    def get_success_url(self):
        return reverse("poll_detail_view", kwargs={"pk": self.object.question.pk})


class PollChoiceDelete(DeleteView):
    template_name = 'choice/delete.html'
    model = Choice

    def get_success_url(self):
        return reverse("poll_detail_view", kwargs={"pk": self.object.question.pk})
