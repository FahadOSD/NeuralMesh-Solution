from django.contrib import admin
from django.urls import path, include
from app.views import (
    index,
    contact_form,
    blog_detail,
    blogs
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('contact/', contact_form, name="contact_form"),
    path('blog-detail/<blog_id>/', blog_detail, name="blog_detail"),
    path('blogs/' , blogs, name="blogs"), 
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]
