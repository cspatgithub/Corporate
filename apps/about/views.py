from django.shortcuts import render

from .models import Detail
from apps.team.models import Staff
from apps.services.models import Service


def About(request):
    details = Detail.objects.all()
    staff = Staff.objects.all()[:3]
    services = Service.objects.all()[:4]


    context = {'details': details, 'staff': staff, 'services': services}

    return render(request, 'about/about.html', context=context)

