from django import forms

from webapp.models import Poll, Choice
from django.forms import widgets


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = '__all__'
        widgets = {
            'question_text': widgets.Input(attrs={'size': 40}),
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ['question']
        widgets = {
            'choice_text': widgets.Input(attrs={'size': 30}),
        }
