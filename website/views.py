from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
      
        form = ContactForm(request.POST)
        if form.is_valid():
            form.instance.name = 'Unknown'
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket submitted sucessfuly')
        else:
            messages.add_message(request, messages.ERROR, "Your ticket didn't submit")
    form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    
    else:
        return HttpResponseRedirect('/')

# Create your views here.

def test_view(request):
    return render(request, 'website/test.html')