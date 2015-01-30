from __future__ import unicode_literals
from rest_framework.routers import DefaultRouter
from todo.api.views import ItemViewSet

router = DefaultRouter()
router.register('todo', ItemViewSet)

urlpatterns = router.urls
