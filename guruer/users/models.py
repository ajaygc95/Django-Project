from django.db import models
from PIL import Image

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

def save(self, *args, **kwargs):
    super(Profile, self).save(*args, **kwargs)

    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300:
        output_size = (300,300)
        img.thumbnail(output_size)
        img.save(self.image.path)



# {% extends "landing/base.html" %}
# {% load crispy_forms_tags %}
# {% block content %}
#     <div class="content-section">
#         <form method="POST">
#             {% csrf_token %}
#             <fieldset class="form-group">
#                 <legend class="border-bottom mb-4">Log In</legend>
#                 {{ form|crispy }}
#             </fieldset>
#             <div class="form-group">
#                 <button class="btn btn-outline-info" type="submit">Login</button>
#             </div>
#         </form>
#         <div class="border-top pt-3">
#             <small class="text-muted">
#                 Need An Account? <a class="ml-2" href="{% url 'register' %}">Sign Up Now</a>
#             </small>
#         </div>
#     </div>
# {% endblock content %}

