from django.contrib import admin
from django.urls import path, include
from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView
                    )

urlpatterns = [
    path('home/', PostListView.as_view(), name='landing-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('detail/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('', views.landing, name='landing-landing'),
    path('sidebar/', views.sidebar, name='landing-sidebar'),
    path('base/', views.base, name='landing-base'),
    path('toggler/', views.toggler, name='landing-toggler'),
]