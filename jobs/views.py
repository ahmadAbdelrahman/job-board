from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing job instances.
    """
    queryset = Job.objects.all().order_by('-posted_date')
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):

        serializer.save(company=self.request.user)

