from django.db import models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse

# a tuple for status, 0 or 1 to indicate whether post is draft or published
STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # one-to-many r'ship from the user
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    # helpers
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    # def get_absolute_url(self):
        # messages.success('Thanks for submitting a post! It will be approved and published shortly')
        # return redirect(to='home')
        # return reverse('post_detail', args=(str(self.id)))
        # return f'Thanks for submitting a post {self.author}! It will be approved and published shortly!'


class Comment(models.Model):
    # one-to-many r'ship because one post can have many comments
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default_100x100.png', upload_to='profile_images')
    cat_idol = models.CharField(max_length=80)
    likes = models.CharField(max_length=150)
    dislikes = models.CharField(max_length=150)
    bio = models.TextField()

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()