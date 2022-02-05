from django import forms

from webapp.models import Poll
from django.forms import widgets


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = '__all__'
        widgets = {
            'question_text': widgets.Input(attrs={'size': 40}),
        }
