from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    """List view for projects."""
    projects = Project.objects.all()
    return render(request, 'projects/list.html', {'projects': projects})

def project_detail(request, slug):
    """Detail view for a single project."""
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/detail.html', {'project': project}) 