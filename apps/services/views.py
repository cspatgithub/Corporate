from django.shortcuts import render
from django.views import generic

from .models import Service
from apps.team.models import Staff
from apps.blog.models import Post

def Home(request):
    services = Service.objects.all()[:4]
    staff = Staff.objects.all()[:3]
    blog = Post.objects.all()[:6]

    context = {'services': services, 'staff': staff, 'posts': blog}

    return render(request, 'services/home.html', context=context)


def Services(request):
    services = Service.objects.all()

    context = {'services': services}

    return render(request, 'services/services.html', context=context)
