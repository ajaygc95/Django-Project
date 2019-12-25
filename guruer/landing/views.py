from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView,

                                  View)
from .models import Detail
from django.contrib import messages

from newcart.models import Order
from django.core.exceptions import ObjectDoesNotExist
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
    template_name = 'landing/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Detail.objects.filter(author=user).order_by('date')


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Detail
    fields = ['client_name', 'address','type','price','liquor_yes','img']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Detail
    fields = ['client_name', 'address','type','liquor_yes','img']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDetailView(DetailView):
    model = Detail

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Detail
    success_url = '/home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'landing/item_list.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/home")


def sidebar(request):
    return render(request, 'landing/sidebar.html')


def landing(request):
    return render(request, 'landing/landing.html')



def base(request):
    return render(request, 'landing/base.html')



def checkout(request):
    return render(request, 'landing/checkout.html')


def toggler(request):
    return render(request, 'landing/toggler.html')