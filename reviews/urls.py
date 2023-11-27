from rest_framework.routers import DefaultRouter

from reviews.apps import ReviewsConfig
from reviews.views import ReviewViewSet

app_name = ReviewsConfig.name

router = DefaultRouter()
router.register(r'', ReviewViewSet, basename='reviews')

urlpatterns = router.urls