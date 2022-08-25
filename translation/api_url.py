from rest_framework import routers

from news.views import NewsViewSet

router: routers.DefaultRouter = routers.DefaultRouter()
router.register('news', NewsViewSet, basename='news')
