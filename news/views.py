from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from news.models import News
from news.serializer import NewsSerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    # def get_queryset(self):
    #     user_language = self.request.GET.get('language')
    #     return News.objects.get_language(user_language).all()
