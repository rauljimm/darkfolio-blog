from django.db import models
from django.urls import reverse
import markdown
import bleach

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github = models.URLField(blank=True)
    url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('projects:project_detail', args=[self.slug])
    
    def short_description(self):
        """Return a short version of the description rendered as HTML from markdown"""
        allowed_tags = [
            'p', 'strong', 'em', 'ul', 'ol', 'li', 'br', 'code', 'a'
        ]
        allowed_attributes = {
            'a': ['href', 'title'],
        }
        
        # Convert markdown to HTML
        html_description = markdown.markdown(self.description, extensions=['fenced_code', 'tables'])
        
        # Sanitize HTML
        safe_html = bleach.clean(html_description, tags=allowed_tags, attributes=allowed_attributes)
        
        # Extract first paragraph or first 20 words, whichever is shorter
        paragraphs = safe_html.split('</p>')
        if len(paragraphs) > 0:
            first_paragraph = paragraphs[0] + '</p>' if '</p>' not in paragraphs[0] else paragraphs[0]
            words = first_paragraph.split()
            if len(words) > 20:
                return ' '.join(words[:20]) + '...'
            return first_paragraph
        
        # Fallback to word count if no paragraphs
        words = safe_html.split()
        if len(words) > 20:
            return ' '.join(words[:20]) + '...'
            
        return safe_html

    def get_description_as_markdown(self):
        """Render description markdown to HTML, sanitizing it first."""
        allowed_tags = [
            'p', 'strong', 'em', 'ul', 'ol', 'li', 'br', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
            'code', 'pre', 'a', 'img', 'blockquote', 'hr'
        ]
        allowed_attributes = {
            'a': ['href', 'title'],
            'img': ['src', 'alt', 'title'],
        }
        html_description = markdown.markdown(self.description, extensions=['fenced_code', 'codehilite', 'tables'])
        safe_html = bleach.clean(html_description, tags=allowed_tags, attributes=allowed_attributes)
        return safe_html 