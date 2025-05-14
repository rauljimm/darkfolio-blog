#!/usr/bin/env python
"""
Demo data population script for DarkFolio Django portfolio
"""
import os
import sys
import django
import random
from datetime import timedelta
from io import BytesIO

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
django.setup()

# Import models after Django setup
from django.utils import timezone
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
import requests
from posts.models import Post
from projects.models import Project

IMAGES = [
    "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
]

def get_random_image():
    """Download a random image from the list and return its content"""
    url = random.choice(IMAGES)
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            filename = url.split('/')[-1].split('?')[0]
            return filename, BytesIO(response.content)
        return None, None
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None, None

def create_superuser():
    """Create a superuser if it does not exist"""
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
            print("✅ Superuser created successfully")
            return True
        else:
            print("ℹ️ Superuser already exists")
            return False
    except Exception as e:
        print(f"❌ Error creating superuser: {e}")
        return False

def create_posts():
    """Create sample blog posts"""
    posts_data = [
        {
            "title": "Getting Started with Django",
            "body": """Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

In this post, we'll cover the basics of Django and how to set up your first project. Django follows the "batteries-included" philosophy and provides everything needed for development, from ORM for database access to template systems for generating HTML.

### Installation

To install Django, you can use pip:
```
pip install django
```

### Starting a New Project

Once installed, you can create a new project:
```
django-admin startproject mysite
```

This will create a directory structure for your project with settings, URL configuration, and more.

### Creating an App

Django uses the concept of "apps" for modularity:
```
python manage.py startapp myapp
```

### Running the Development Server

```
python manage.py runserver
```

This will start a development server at http://127.0.0.1:8000/

Django is perfect for both small projects and large-scale applications, with excellent documentation and a supportive community.""",
            "status": "published",
            "publish": timezone.now() - timedelta(days=12),
        },
        {
            "title": "Python Tips and Tricks for Developers",
            "body": """Python is one of the most popular programming languages, known for its simplicity and readability. Whether you're a beginner or an experienced developer, there are always new tricks to learn.

Here are some useful Python tips and tricks that can help you write more efficient and cleaner code:

### 1. List Comprehensions

Instead of:
```python
squares = []
for i in range(10):
    squares.append(i * i)
```

You can write:
```python
squares = [i * i for i in range(10)]
```

### 2. Unpacking

Swap variables without a temporary variable:
```python
a, b = b, a
```

### 3. Enumerate

When you need the index and value:
```python
for i, value in enumerate(my_list):
    print(f"Index {i}: {value}")
```

### 4. Dictionary Comprehensions

Create dictionaries on the fly:
```python
squares = {i: i * i for i in range(10)}
```

### 5. Default Dictionaries

Never worry about key errors:
```python
from collections import defaultdict
dd = defaultdict(int)  # Default value of 0 for new keys
```

These are just a few examples of the elegant features Python offers. Keep exploring the language and you'll discover many more useful patterns and techniques!""",
            "status": "published",
            "publish": timezone.now() - timedelta(days=8),
        },
        {
            "title": "Building Responsive Websites with Bootstrap",
            "body": """Bootstrap is one of the most popular CSS frameworks for building responsive, mobile-first websites. It provides a collection of CSS and JavaScript tools to help you quickly design and customize responsive websites.

### Getting Started with Bootstrap

Adding Bootstrap to your project is easy. You can either download the files or use a CDN:

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```

### Responsive Grid System

Bootstrap's grid system is based on a 12-column layout and five default responsive tiers:

```html
<div class="container">
  <div class="row">
    <div class="col-sm-4">Column 1</div>
    <div class="col-sm-4">Column 2</div>
    <div class="col-sm-4">Column 3</div>
  </div>
</div>
```

### Components

Bootstrap includes numerous components like navigation bars, cards, modals, and carousels:

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <!-- Navbar content -->
</nav>

<div class="card">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Card content</p>
  </div>
</div>
```

### Utilities

Bootstrap provides utilities for typography, spacing, colors, and more:

```html
<p class="text-primary">Primary text</p>
<div class="mt-4 p-3 bg-light">Spaced and padded</div>
```

With Bootstrap, you can quickly build responsive websites without having to write a lot of CSS. It's particularly useful for prototypes and projects where custom design isn't the main priority.""",
            "status": "published",
            "publish": timezone.now() - timedelta(days=5),
        },
        {
            "title": "Deploying with Docker: A Beginner's Guide",
            "body": """Docker has revolutionized how we deploy applications by providing a consistent environment from development to production. In this guide, we'll explore the basics of Docker and how to use it for deployment.

### What is Docker?

Docker is a platform that uses containerization to package applications and their dependencies together. This ensures that your application works the same way in every environment.

### Key Concepts

- **Images**: Read-only templates with instructions for creating containers
- **Containers**: Running instances of images
- **Dockerfile**: Text document with instructions to build an image
- **Docker Compose**: Tool for defining multi-container applications

### Creating a Dockerfile

Here's a simple Dockerfile for a Python application:

```dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Building and Running

Build your Docker image:
```bash
docker build -t myapp .
```

Run a container from the image:
```bash
docker run -p 8000:8000 myapp
```

### Docker Compose

For multi-container applications, use Docker Compose:

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "8000:8000"
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: password
```

Run with:
```bash
docker-compose up
```

Docker simplifies deployment and ensures consistency across different environments, making it easier to develop, test, and deploy applications.""",
            "status": "published",
            "publish": timezone.now() - timedelta(days=2),
        },
    ]

    posts_created = 0
    for post_data in posts_data:
        if not Post.objects.filter(title=post_data["title"]).exists():
            # Create a slug-friendly version of the title
            import re
            slug = post_data["title"].lower()
            # Replace special characters, spaces, and punctuation with hyphens
            slug = re.sub(r'[^\w\s-]', '', slug)  # Remove special characters
            slug = re.sub(r'\s+', '-', slug)      # Replace spaces with hyphens
            slug = re.sub(r'--+', '-', slug)      # Replace multiple hyphens with single hyphen
            
            post = Post.objects.create(
                title=post_data["title"],
                slug=slug,
                body=post_data["body"],
                status=post_data["status"],
                publish=post_data["publish"],
            )
            
            # Add image to post if possible
            filename, image_content = get_random_image()
            if filename and image_content:
                image_name = f"{post.slug}_{filename.split('.')[0]}"
                post.image.save(
                    f"{image_name}", 
                    ContentFile(image_content.read()), 
                    save=True
                )
            
            posts_created += 1
    
    print(f"✅ Created {posts_created} blog posts")
    return posts_created > 0

def create_projects():
    """Create sample projects"""
    projects_data = [
        {
            "title": "Personal Blog with Django",
            "slug": "personal-blog-with-django",
            "description": """A personal blog built with Django featuring a responsive design, comment system, and admin dashboard. This project demonstrates my understanding of Django's MVT architecture and includes features like user authentication, comment moderation, and SEO optimization.

The blog includes categories and tags for organizing content, an integrated search feature, and a customizable theme. It leverages Django's ORM for database operations and the template system for rendering dynamic content.""",
            "featured": True,
            "github": "https://github.com/yourusername/django-blog",
            "url": "https://django-blog-demo.example.com",
        },
        {
            "title": "Social Network with React and Django",
            "slug": "social-network-with-react-and-django",
            "description": """A social network application built with React frontend and Django REST framework backend. Features include user profiles, posts, comments, likes, and real-time chat using WebSockets.

The frontend uses React hooks, context API for state management, and styled components for styling. The backend provides a RESTful API with JWT authentication, and uses Django channels for the real-time features. The application is fully responsive and offers a dark mode option.""",
            "featured": True,
            "github": "https://github.com/yourusername/social-network",
            "url": "https://social-network-demo.example.com",
        },
        {
            "title": "Image Classifier with TensorFlow",
            "slug": "image-classifier-with-tensorflow",
            "description": """An image classification application that uses TensorFlow to identify objects in images. The model is trained on a custom dataset and can recognize over 100 different objects with high accuracy.

The project includes a web interface built with Flask where users can upload images for classification. It also features API endpoints for integrating the classifier into other applications. The model was trained using transfer learning on a pre-trained MobileNetV2 architecture.""",
            "featured": False,
            "github": "https://github.com/yourusername/image-classifier",
        },
    ]

    projects_created = 0
    for project_data in projects_data:
        if not Project.objects.filter(title=project_data["title"]).exists():
            project = Project.objects.create(
                title=project_data["title"],
                slug=project_data["slug"],
                description=project_data["description"],
                featured=project_data["featured"],
                github=project_data.get("github", ""),
                url=project_data.get("url", ""),
            )
            
            # Add image to project if possible
            filename, image_content = get_random_image()
            if filename and image_content:
                image_name = f"{project.slug}_{filename.split('.')[0]}"
                project.image.save(
                    f"{image_name}", 
                    ContentFile(image_content.read()), 
                    save=True
                )
            
            projects_created += 1
    
    print(f"✅ Created {projects_created} projects")
    return projects_created > 0

def main():
    """Main function to run the population script"""
    print("\n=== 🔍 Checking for existing data... ===\n")
    
    # Count existing data
    existing_posts = Post.objects.count()
    existing_projects = Project.objects.count()
    
    print(f"Found {existing_posts} posts and {existing_projects} projects")
    
    print("\n=== 🌱 Populating database with demo data... ===\n")
    
    # Create a superuser
    create_superuser()
    
    # Create sample data
    posts_created = create_posts()
    projects_created = create_projects()
    
    # Summary
    if posts_created or projects_created:
        print("\n=== ✅ Demo data created successfully! ===\n")
        print("You can now log in to the admin panel with:")
        print("Username: admin")
        print("Password: admin1234")
        print("\nVisit the site at http://127.0.0.1:8000/")
    else:
        print("\n=== ℹ️ No new data was created (database already has content) ===\n")

if __name__ == '__main__':
    main() 