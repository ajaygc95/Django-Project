from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from landing.models import Detail


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    item = models.ForeignKey(Detail, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return self.item.client_name

    def get_total_item_price(self):
        return round(float(self.quantity * self.item.price),2)

    def get_final_price(self):
        return round(float(self.get_total_item_price()),2)



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def get_total(self):
        total = 0

        for order_item in self.items.all():
            total += order_item.get_final_price()
        return round(float(total),2)

