from django.db import router
from rest_framework import routers
from .views import TodoViewset

router = routers.DefaultRouter()
router.register('todo', TodoViewset)