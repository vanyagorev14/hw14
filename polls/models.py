from django.db import models

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
