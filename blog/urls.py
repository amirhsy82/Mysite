
from django.contrib import admin
from django.urls import path
# form "Priject's Directory"."FileName" import "function"
from blog.views import *


app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    # path('post-<int:pid>', test, name='test'),
]
