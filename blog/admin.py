from django.contrib import admin
from .models import Post, Comment, Profile
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Profile)


# this decorator tells where in admin we want to use summernote
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    # configurations to add functionality to admin panel
    # list_display = ('title', 'slug', 'status', 'created_on')
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'created_on')
    # list_filter = ('status', 'created_on')
    summernote_fields = ('content')

# this method can only take two arguments so gets full too quickly so we use a decorator instead
# admin.site.register()

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    # actions method is built-in feature of admin classes
    # actions takes list of function names as arguments
    actions = ['approve_comments']

    # creating approve_comments method
    def approve_comments(self, request, queryset):
        # queryset is what is used to update the record
        queryset.update(approved=True)
