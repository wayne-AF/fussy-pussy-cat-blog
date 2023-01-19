from . import views
from .views import profile, AddPostView
from django.urls import path


urlpatterns = [
    # because using class-based views, must use as_view() after PostList so it will render the class as a view
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('profile/', profile, name='user_profile'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    

]