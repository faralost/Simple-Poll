# Generated by Django 4.0.2 on 2022-02-05 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_choice_options_alter_poll_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='webapp.poll', verbose_name='Вопрос'),
        ),
    ]
