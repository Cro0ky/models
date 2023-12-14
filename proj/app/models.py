from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    password = models.CharField(max_length=50)
    email = models.EmailField()
    url = models.URLField()

    def __str__(self):
        return f'{self.name} {self.age}'


class Posts(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    content = models.TextField(verbose_name='Content')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
