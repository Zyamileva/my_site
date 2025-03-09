from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def post_view(request, id):
    return render(request, 'post.html', {'post_id': id})

def profile_view(request, username):
    return render(request, 'profile.html',{'username': username})

def event_view(request, year, month, day):
    return render(request, 'event.html', {'year': year, 'month': month, 'day': day})


