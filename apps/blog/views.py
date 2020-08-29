from django.shortcuts import render
from django.views import generic
from django.db.models import Q

from .models import Post


class Blog(generic.ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(Blog, self).get_context_data(**kwargs)
        context['posts_count'] = Post.objects.all().count()
        return context


class PostDetail(generic.View):
   
   def get(self, request, *args, **kwargs):
        post = Post.objects.get(slug=self.kwargs['slug'])
        other_posts = Post.objects.exclude(slug=self.kwargs['slug'])[:5]

        context = {'post': post, "other_posts": other_posts}

        return render(request, 'blog/post_detail.html', context=context)


class SearchResults(generic.ListView):
    model = Post
    template_name = 'blog/search.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(SearchResults, self).get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['results'] = Post.objects.filter(Q(title__icontains=query))
        return context