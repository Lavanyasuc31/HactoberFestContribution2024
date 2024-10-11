from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('remote', 'Remote'),
    ]

    role = models.CharField(max_length=400)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default='india')
    link_to_original_source = models.URLField(unique=True)
    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES)

    def __str__(self):
        return f"{self.role} at {self.company_name}"
    

class Profile(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('remote', 'Remote'),
    ]

    JOB_TITLE_CHOICES = [
        ('django/python developer', 'Django/Python Developer'),
        ('ui ux designer', 'UI UX Designer'),
        ('project manager', 'Project Manager'),
        ('full stack web developer', 'Full Stack Web Developer'),
        ('mern stack developer', 'MERN Stack Developer'),
        ('artificial intelligence(ai) and machine learning(ml) engineer', 'AI/ML Engineer'),
        ('data scientist/analyst', 'Data Scientist/Analyst'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="Profile_photos", null=True, blank=True)
    age = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    preferred_job_title = models.CharField(max_length=100, choices=JOB_TITLE_CHOICES)
    preferred_job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES)
    preferred_job_location = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False) 

    def __str__(self):
        return  self.user.username
    
    @property
    def displayname(self):
        if self.name:
            return self.name
        return self.user.username 
    
    @property
    def avatar(self):
        if self.image:
            return self.image.url
        return f'{settings.STATIC_URL}images/avatar.svg' 
        # return static('images/avatar.svg')
        