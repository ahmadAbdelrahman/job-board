from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):

    queryset = Application.objects.all().order_by('-applied_at')
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]


    # Ensure the candidate field is set from the logged-in user

    def perform_create(self, serializer):
        # Automatically set the applicant to the current user
        serializer.save(candidate=self.request.user)

        #test
