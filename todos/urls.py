from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TodoViewSet


app_name = "todos"

router = DefaultRouter()
router.register("", TodoViewSet, "todos")

urlpatterns = [
    path("", include(router.urls))
]