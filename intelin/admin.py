from django.contrib import admin
from .models import Argument, Refute

class ArgumentAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']
    search_help_text = ('*제목 또는 내용을 검색하시오.')
    fields = ('content',)


admin.site.register(Argument, ArgumentAdmin)
