from rest_framework.routers import DefaultRouter
from api.views import AssignmentViewSet

router = DefaultRouter()
router.register('assignment', AssignmentViewSet)
urlpatterns = router.urls
