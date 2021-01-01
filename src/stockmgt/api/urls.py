from rest_framework import routers
from .views import ListViewSet

router = routers.SimpleRouter()
router.register(r'list', ListViewSet)
urlpatterns = router.urls