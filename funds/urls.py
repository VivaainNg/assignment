from rest_framework.routers import DefaultRouter

from .views import FundViewSet

app_name = "funds"

router = DefaultRouter()
router.register("", FundViewSet, basename="funds")

# Base url for the Fund's apps within the project
urlpatterns = router.urls
