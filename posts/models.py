from django.db import models
from django.utils import timezone
from django.urls import reverse
import markdown
import bleach

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    image = models.ImageField(upload_to='posts/%Y/%m/%d/', blank=True, null=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
        ])
        
    def short_body(self):
        """Return a short version of the body rendered as HTML from markdown"""
        # Convert markdown to HTML with limited number of words
        allowed_tags = [
            'p', 'strong', 'em', 'ul', 'ol', 'li', 'br', 'code', 'a'
        ]
        allowed_attributes = {
            'a': ['href', 'title'],
        }
        
        # Convert markdown to HTML
        html_body = markdown.markdown(self.body, extensions=['fenced_code', 'tables'])
        
        # Sanitize HTML
        safe_html = bleach.clean(html_body, tags=allowed_tags, attributes=allowed_attributes)
        
        # Extract first paragraph or first 25 words, whichever is shorter
        paragraphs = safe_html.split('</p>')
        if len(paragraphs) > 0:
            first_paragraph = paragraphs[0] + '</p>' if '</p>' not in paragraphs[0] else paragraphs[0]
            words = first_paragraph.split()
            if len(words) > 30:
                return ' '.join(words[:30]) + '...'
            return first_paragraph
        
        # Fallback to word count if no paragraphs
        words = safe_html.split()
        if len(words) > 30:
            return ' '.join(words[:30]) + '...'
            
        return safe_html

    def get_body_as_markdown(self):
        """Render body markdown to HTML, sanitizing it first."""
        # Allowed HTML tags and attributes for bleach
        allowed_tags = [
            'p', 'strong', 'em', 'ul', 'ol', 'li', 'br', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
            'code', 'pre', 'a', 'img', 'blockquote', 'hr'
        ]
        allowed_attributes = {
            'a': ['href', 'title'],
            'img': ['src', 'alt', 'title'],
        }
        # Convert markdown to HTML
        html_body = markdown.markdown(self.body, extensions=['fenced_code', 'codehilite', 'tables'])
        # Sanitize HTML
        safe_html = bleach.clean(html_body, tags=allowed_tags, attributes=allowed_attributes)
        return safe_html 