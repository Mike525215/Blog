from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    blog_photo = models.ImageField(upload_to='photos/')
    time_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'blog_id': self.pk})