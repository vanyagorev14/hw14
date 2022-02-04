from django.db import models
from django.contrib.auth import get_user_model

class Author(models.Model):
    name = models.CharField(max_length=150)
    birthday = models.CharField(max_length=150)
    birth_loc = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name, self.description, self.birthday


class Citate(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.text, self.author

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    brief_desc = models.CharField(max_length=150)
    publish_datae = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    full_desc = models.CharField(max_length=150)
    posted = models.BooleanField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    username = models.CharField(max_length=150)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_on = models.BooleanField()

    def __str__(self):
        return self.text