from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)
from .models import Detail
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

def home(request):

    posts = Detail.objects.all()


    return render(request,'landing/home.html', {'posts':posts})

class PostListView(ListView):
    model = Detail
    template_name = 'landing/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date']

class UserPostListView(ListView):
    model = Detail
    template_name = 'landing/user_detail.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'


    def get_queryset(self):
        user1 = get_object_or_404(User,username=self.kwargs.get('username'))
        return Detail.objects.filter(user=user1).order_by('-date')




class PostCreateView(LoginRequiredMixin,CreateView):
    model = Detail
    fields = ['client_name', 'address','type','liquor_yes','img']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Detail
    fields = ['client_name', 'address','type','liquor_yes','img']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Detail
    success_url = 'home/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostDetailView(DetailView):
    model = Detail



def sidebar(request):
    return render(request, 'landing/sidebar.html')


def landing(request):
    return render(request, 'landing/landing.html')



def base(request):
    return render(request, 'landing/base.html')


def toggler(request):
    return render(request, 'landing/toggler.html')