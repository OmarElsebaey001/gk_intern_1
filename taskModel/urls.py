
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from . import views
from rest_framework_nested.routers import DefaultRouter,NestedDefaultRouter

router=DefaultRouter()
router.register('models',views.ModelsViewSet)
router.register('versions',views.VersionsViewSet)
versionsRouter=NestedDefaultRouter(router,'versions',lookup='version')  # lookup-> versions_id,versions_name
versionsRouter.register('allocation_items',views.AllocationItemViewSet,basename='versions-allocationItems')


urlpatterns = router.urls + versionsRouter.urls