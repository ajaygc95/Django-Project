from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect, reverse
from landing.models import Detail
from django.utils import timezone
from django.views.generic import ListView
from .models import OrderItem, Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.




@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Detail, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("item-list")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("item-list")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("item-list")



# def add_item_cart(request, slug):
#     item = get_object_or_404(Detail, slug=slug)
#     order_item, created = OrderItem.objects.get_or_create(
#         item=item,
#         user=request.user,
#         ordered=False
#     )
#     order_qs = Order.objects.filter(user=request.user, ordered=False)
#
#     if order_qs.exists():
#         order = order_qs[0]
#
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item.quantity += 1
#             order_item.save()
#             messages.info(request, "This item quantity was updated.")
#         else:
#             order.items.add(order_item)
#             messages.info(request, "This item is added to your cart.")
#
#     else:
#         ordered_date = timezone.now()
#         messages.info(request, "This item is added to your cart.")
#         order = Order.objects.create(user=request.user, ordered_date=ordered_date)
#         order.item.add(order_item)
#     return redirect('post-detail',slug= slug )
#
@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Detail, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect('item-list')
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('item-list')
    else:
        messages.info(request, "You do not have an active order")
        return redirect('item-list')

@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Detail, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("item-list")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("item-list", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("item-list", slug=slug)