from django.db import IntegrityError
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from webapp.models import Poll, Choice, Answer


class AnswerView(TemplateView):
    template_name = 'answer/answer.html'

    def get_context_data(self, **kwargs):
        context = super(AnswerView, self).get_context_data(**kwargs)
        question = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        context['question'] = question
        context['poll_choices'] = question.choices.all()
        context['poll_count'] = self.get_polls_count()
        context['choices_count'] = self.get_choices_count()
        return context

    def post(self, request, *args, **kwargs):
        Answer.objects.create(question_id=self.kwargs.get('pk'), choice_id=self.request.POST.get('choice_pk'))
        nexttt = request.POST.get('next', '/')
        return redirect(nexttt)

    def get_polls_count(self):
        polls_count = Answer.objects.filter(question_id=self.kwargs.get('pk')).count()
        return polls_count

    def get_choices_count(self):
        choices_count = Answer.objects.filter(question_id=self.kwargs.get('pk')).values('choice_id').annotate(
            choice_count=Count('choice_id'))
        return choices_count

    def get_percentage_of_choices(self):
        pass
