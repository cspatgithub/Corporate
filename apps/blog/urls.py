from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.Blog.as_view(), name='blog'),
    path('blog/<slug:slug>', views.PostDetail.as_view(), name='post-detail'),
    path('blog/search/', views.SearchResults.as_view(), name='search-results')
]