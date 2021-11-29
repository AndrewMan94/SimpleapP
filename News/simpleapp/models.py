from django.db import models

class News(models.Model):
    title = models.CharField(max_length=128, unique=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField()
    post = models.ForeignKey(
        to='Post',
        on_delete=models.CASCADE,
        related_name='news',
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description [:20]}'

class Post(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f'{self.name.title()}'