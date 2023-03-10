from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Post, Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm, EditProfileForm, CreatePostForm, UpdatePostForm, ChangePasswordForm, UpdateProfileForm


class ProfilePageView(LoginRequiredMixin, DetailView):
    """
    View for viewing a user's profile page
    """
    model = Profile
    template_name = 'user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)

        profile_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["profile_user"] = profile_user
        return context


class PasswordsChangeView(LoginRequiredMixin, PasswordChangeView):
    """
    View for changing the user's password
    """
    form_class = ChangePasswordForm
    success_url = reverse_lazy('password_success')
    

@login_required
def password_success(request):
    """
    Renders a success message when the user changes their password
    """
    return render(request, 'password_success.html', {})


class PostList(generic.ListView):
    """
    Displays a list of 6 most recent posts
    """
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """
    View for seeing the content of a post, including 
    its comments and likes, with a link to view the author's
    profile
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class PostLike(LoginRequiredMixin, View):
    """
    View for displaying the number of likes on a post
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def contact(request):
    """
    View for a contact form 
    """
    return render(request, 'contact.html', {})


class AddPostView(LoginRequiredMixin, CreateView):
    """
    View for a user to write and upload a post
    """
    model = Post
    form_class = CreatePostForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    """
    View for user to update a post they have written
    """
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'


class DeletePostView(LoginRequiredMixin, DeleteView):
    """
    View for a user to delete a post they have written
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class UserEditView(LoginRequiredMixin, UpdateView):
    """
    View for a user to edit their username and email.
    Also provides a link for user to update their password
    """
    model = User
    form_class = EditProfileForm
    template_name = 'edit_account.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class EditProfilePageView(LoginRequiredMixin, UpdateView):
    """
    View for a user to edit their profile page
    """
    model = Profile
    template_name = 'edit_profile.html'
    form_class = UpdateProfileForm
    success_url = reverse_lazy('home')
