from modeltranslation.translator import register, TranslationOptions

from .models import News


@register(News)
class NewsTranslationOption(TranslationOptions):
    fields = ('title', 'content')

