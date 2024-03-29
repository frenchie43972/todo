from .serializers import TaskSerializers
from .models import Task
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  serializer_class = TaskSerializers