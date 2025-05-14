from django.shortcuts import render
from posts.models import Post
from projects.models import Project

def home(request):
    """Home page view showing featured projects and latest posts."""
    posts = Post.objects.filter(status='published').order_by('-publish')[:3]
    projects = Project.objects.filter(featured=True)[:3]
    return render(request, 'home.html', {'posts': posts, 'projects': projects})

def about(request):
    """About page view."""
    return render(request, 'about.html') 