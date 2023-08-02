from django.db.models.signals import pre_save , post_save
from django.dispatch import receiver
from product.models import ProductVersion
from django.utils.text import slugify



@receiver(post_save , sender = ProductVersion)
def slug(sender , instance ,created, *args , **kwargs):
    slug = slugify(instance.product_id) + str(instance.id)

    if not slug == instance.slug:
        instance.slug = slug
        instance.save()