
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from . import views


router=SimpleRouter()
router.register('models',views.ModelsViewSet)
router.register('versions',views.VersionsViewSet)


urlpatterns = router.urls