from django.db import models
from django.conf import settings
from PIL import Image
from django.urls import reverse

class Detail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    type = models.CharField(max_length=100)
    liquor_yes = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='pics',default='default.img')


    def __str__(self):
        return self.client_name


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})
