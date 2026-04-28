from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

class TaskStatusSummaryAPIView(APIView):
    """
    Returns the count of tasks grouped by status.
    Useful for data visualizations like pie charts.
    """
    def get(self, request):
        summary = Task.objects.values('status').annotate(count=Count('id')).order_by('status')
        return Response(summary)
