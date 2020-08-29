from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages

from .models import Contact
from apps.blog.models import Post
from .forms import ContactForm


def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Message sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
        blog = Post.objects.all()[:6]
    return render(request, 'contact/contact.html', {'form': form, 'blog': blog})

    
