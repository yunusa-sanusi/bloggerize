from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from tinymce.models import HTMLField

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    post_image = models.ImageField(upload_to='images/post_image')
    content = HTMLField()
    views = models.IntegerField(default=0)
    categories = models.ManyToManyField('Tag', related_name='tags')
    date_published = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(unique=True, always_update=True,
                         populate_from='title')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('posts:post-update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('posts:post-delete', kwargs={'slug': self.slug})

    @property
    def image_url(self):
        try:
            image = self.post_image.url
        except:
            image = ''
        return image


class Category(models.Model):
    category = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(max_length=20)
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tag
