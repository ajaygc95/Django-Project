from django.contrib import admin
from django.urls import path, include
from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    OrderSummaryView,
                    )

urlpatterns = [
    path('home/', PostListView.as_view(), name='landing-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<slug>/', PostDetailView.as_view(), name='post-detail'),
    path('detail/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('', views.landing, name='landing-landing'),
    path('sidebar/', views.sidebar, name='landing-sidebar'),
    path('base/', views.base, name='landing-base'),
    path('toggler/', views.toggler, name='landing-toggler'),
    path('item-list/', OrderSummaryView.as_view(), name='item-list'),
    path('checkout/', views.checkout, name='item-checkout'),

    path('social/', include('social_django.urls', namespace='social')),

]

