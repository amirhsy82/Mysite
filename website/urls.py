
from django.contrib import admin
from django.urls import path
# form "Priject's Directory"."FileName" import "function"
from website.views import index_view, about_view, contact_view

urlpatterns = [
    path('', index_view),
    path('about', about_view),
    path('contact', contact_view)
]
