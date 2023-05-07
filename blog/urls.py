
from django.contrib import admin
from django.urls import path
# form "Priject's Directory"."FileName" import "function"
from blog.views import blog_view, blog_single

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('single', blog_single, name='single')
]
