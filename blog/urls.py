from . import views
from .views import AddPostView, UpdatePostView, DeletePostView, UserEditView, PasswordsChangeView, ProfilePageView, EditProfilePageView
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('edit_account/<int:user_id>/', views.UserEditView.as_view(), name='edit_account_page'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('edit/<slug:slug>/', UpdatePostView.as_view(), name='update_post'),
    path('delete/<slug:slug>/', DeletePostView.as_view(), name='delete_post'),
    path('edit_account/password/', PasswordsChangeView.as_view(template_name='change-password.html')),
    path('password/password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile_page_view'),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name='edit_profile_page'),

]