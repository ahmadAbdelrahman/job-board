from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    EMPLOYMENT_TYPES = (
        ('full-titm', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField
    location = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPES)
    company = models.ForeignKey(User, on_delete=models.CASCADE)  # The employer posting the job
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

