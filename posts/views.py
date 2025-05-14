from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def post_list(request):
    """List view for blog posts with pagination."""
    posts_list = Post.objects.filter(status='published')
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        posts_list = posts_list.filter(title__icontains=search_query) | \
                     posts_list.filter(body__icontains=search_query)
    
    # Pagination
    paginator = Paginator(posts_list, 6)  # 6 posts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'posts/list.html', {'posts': posts})

def post_detail(request, year, month, day, slug):
    """Detail view for a single blog post."""
    post = get_object_or_404(Post, 
                            slug=slug,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    
    # Get related posts
    related_posts = Post.objects.filter(status='published').exclude(id=post.id)[:3]
    
    return render(request, 'posts/detail.html', {'post': post, 'posts': related_posts}) 