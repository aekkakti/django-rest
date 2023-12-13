from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('test/', include('rest_framework.urls', namespace='drf_auth'))
] + static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)