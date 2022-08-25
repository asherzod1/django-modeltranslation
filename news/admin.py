from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from news.models import News


class NewsAdmin(TranslationAdmin):
    list_display = ['title', 'content']


admin.site.register(News, NewsAdmin)
