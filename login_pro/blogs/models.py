from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=30, help_text='title should be short')
    content = models.TextField(help_text='Keep the blog content descriptive')
    created_by = models.CharField(max_length=20)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
