from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from webapp.models import Poll, Choice, Answer


class AnswerView(TemplateView):
    template_name = 'answer/answer.html'

    def get_context_data(self, **kwargs):
        context = super(AnswerView, self).get_context_data(**kwargs)
        question = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        context['question'] = question
        poll_choices = question.choices.all()
        context['poll_choices'] = poll_choices
        return context

    def post(self, request, *args, **kwargs):
        Answer.objects.create(question_id=self.kwargs.get('pk'), choice_id=self.request.POST.get('choice_pk'))
        nexttt = request.POST.get('next', '/')
        return redirect(nexttt)
