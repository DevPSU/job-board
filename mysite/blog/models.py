from django.db import models
from django.contrib.auth.models import User
import random
import string

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default=''.join(random.choices(string.ascii_uppercase + string.digits, k=50)))
    description = models.CharField(max_length=800, default="Give a brief description")
    contact = models.CharField(max_length=200, default="Leave an email or phone number")
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    additional_information = models.TextField(default="Provide any additional information that would be useful")
    
    STUDY_GROUP = 'Study Group'
    GROUP_PROJECT = 'Group Project'
    JOB = 'Job'
    INTERNSHIP = 'Internship'
    RESEARCH = 'Research'
 
    JOB_TYPES = [
        (GROUP_PROJECT, 'Group Project'),        
        (INTERNSHIP, 'Internship'),
        (JOB, 'Job'),
        (RESEARCH, 'Research'),
        (STUDY_GROUP, 'Study Group')
    ]

    job_type = models.CharField(
        max_length=15,
        choices=JOB_TYPES,
        default=GROUP_PROJECT,
    )

    created_on = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
