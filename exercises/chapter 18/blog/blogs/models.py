from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    """A blog that can multiple blog posts."""
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """A string representation of a Blog model."""
        return self.title

class Post(models.Model):
    """A single blog post."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """A string representation of a post model."""
        return self.title