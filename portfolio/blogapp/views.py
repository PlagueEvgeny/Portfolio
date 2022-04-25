from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Post

class PostList(ListView):
    model = Post
    paginate_by=10
    
    def get_queryset(self):
        if "search" in self.request.GET:
        	search_title = self.request.GET["search"]
        	queryset = Post.objects.filter(status=1).order_by('-created_at')
        	return queryset.filter(title__icontains=search_title)
        else:
            queryset = Post.objects.filter(status=1).order_by("-created_at")

        return queryset


class PostDetail(DetailView):
	model = Post
	
