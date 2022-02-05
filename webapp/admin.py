from django.contrib import admin

from webapp.models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'created_at']
    search_fields = ['question_text']
    fields = ['question_text', 'created_at']
    readonly_fields = ['created_at']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Answer)
