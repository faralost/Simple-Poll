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
    choice_text = models.CharField(max_length=250, verbose_name='Вариант ответа')
    question = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name='choices', verbose_name='Вопрос')

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'

    def __str__(self):
        return f'{self.choice_text}'


class Answer(models.Model):
    question = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name='answers', verbose_name='Вопрос')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    choice = models.ForeignKey('webapp.Choice', on_delete=models.CASCADE, related_name='answers',
                               verbose_name='Вариант ответа')

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
