from django.db import models

class Booklist(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    