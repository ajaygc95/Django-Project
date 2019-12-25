import random
import string
from django.utils.text import slugify

# def unique_slug_generator(model_instance,title,slugfiled):
#     slug =slugify(title)
#     model_class = model_instance.__class__
#     while model_class.__default_manager.filter(slug=slug).exists():
#         object_pk = model_class._default_manager.latest('pk')
#         object_pk = object_pk +1
#         slug = f'{slug}-{object_pk}'
#     return slug


def random_string_generator(size=10,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance,new_slug=None):

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.client_name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = '{}-{}'.format(slug,random_string_generator(size=4))

        return unique_slug_generator(instance,new_slug=new_slug)

    return slug
