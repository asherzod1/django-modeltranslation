from django.conf import settings
from django.utils import translation
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class ForceLangMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path == '/':
            request.LANG = getattr(settings, 'LANGUAGE_CODE', settings.LANGUAGE_CODE)
            translation.activate(request.LANG)
            request.LANGUAGE_CODE = request.LANG
            return redirect('/' + request.LANG)
