from django.db import models
from django.urls import reverse


class Poll(models.Model):
    question_text = models.CharField(max_length=250, verbose_name='Вопрос')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'{self.question_text}'

    def get_absolute_url(self):
        return reverse('poll_detail_view', kwargs={'pk': self.pk})


class Choice(models.Model):
    choice_text = models.CharField(max_length=250, verbose_name='Ответ')
    question = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return f'{self.choice_text}'
