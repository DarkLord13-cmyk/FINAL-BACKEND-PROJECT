from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, TaskStatusSummaryAPIView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('summary/tasks/', TaskStatusSummaryAPIView.as_view(), name='task-summary'),
    path('', include(router.urls)),
]
