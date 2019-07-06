from django.contrib import admin
from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView
from blog import views

urlpatterns = [
    # path('', views.home, name='blog-home'), Instead of using function based view now we are using class based view.
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('about/', views.about, name='blog-about'),
]
