from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field


class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=255, default='Company')
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    open_hours = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)  
    
    def __str__(self):
        return self.company_name
 
    
    
class Service(models.Model):
    icon = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    
class Testimonial(models.Model):
    user_image = models.CharField(max_length=255, blank=True, null=True)
    star_count = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    rating_count = models.IntegerField(choices=star_count)
    username = models.CharField(max_length=50)
    user_job_title = models.CharField(max_length=50)
    review = models.TextField()
    
    def __str__(self):
        return f"{self.username} - {self.user_job_title}"  
    
class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    
    def __str__(self):
        return self.question
    
class ContactFormLog(models.Model) :
    name = models.CharField (max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    action_time = models.DateTimeField(null=True, blank=True)
    is_success = models.BooleanField (default=False)
    is_error = models.BooleanField (default=False)
    error_message = models.TextField (null=True, blank=True)
    
    def _str_(self):
        return self.email


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50)
    joined_at = models.DateTimeField(null=True, blank=True)

    def __str__(self): 
        return self.first_name


class Blog(models.Model):
    blog_image = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, null=True)
    create_at = models.DateTimeField(default=timezone.now)
    content = CKEditor5Field('Content', config_name='default')#models.TextField()
    
    def _str_(self):
        return self.title
        