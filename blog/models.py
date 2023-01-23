from django.db import models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from ckeditor.fields import RichTextField

# class SomeForm(forms.Form):
#     foo = SummernoteTextFormField()


# a tuple for status, 0 or 1 to indicate whether post is draft or published
STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # one-to-many r'ship from the user
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=True, null=True)
    # content = models.TextField()
    # featured_image = models.ImageField(null=True, blank=True, upload_to='images/')
    # profile_pic = models.ImageField(default='default_100x100.png', upload_to='profile_images', blank=True)

    featured_image = CloudinaryField('image', default='placeholder_featured_image.png')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    # helpers
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    # one-to-many r'ship because one post can have many comments
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    # add this to be able to reference the author of the comment?
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image', default='default_profile_image.png')

    # profile_pic = models.ImageField(default='default_100x100.png', upload_to='profile_images', blank=True)
    breed = models.CharField(max_length=50, blank=True)
    favourite_quote = models.CharField(max_length=200, blank=True)
    likes = models.CharField(max_length=150)
    dislikes = models.CharField(max_length=150)
    about = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username}'


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()