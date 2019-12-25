from django.db import models
from django.contrib.auth.models import User
from guruer.utils import unique_slug_generator
from django.urls import reverse
from django.db.models.signals import pre_save,post_save

class Detail(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250,null=True,blank=True)
    address = models.CharField(max_length=500)
    type = models.CharField(max_length=100)
    liquor_yes = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='pics',default='default.img')
    price = models.FloatField(null=False)

    def __str__(self):
        return self.client_name


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'slug': self.slug})

    def get_add_to_cart(self):
        return reverse('add-to-cart', kwargs={'slug': self.slug})

    def get_remove_from_cart(self):
        return reverse('remove-from-cart',kwargs={'slug':self.slug})


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator,sender=Detail)
