from django.urls import path
from posts import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('create-post/', views.CreatePost.as_view(), name='create-post'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('<slug:slug>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
