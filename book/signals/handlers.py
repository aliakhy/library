from django.conf import settings
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from book.models import *

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_customer_for_new_user(sender, **kwargs):
#   if kwargs['created']:
#     Customer.objects.create(user=kwargs['instance'])


@receiver(post_save, sender=Borrow)
def change_existing_book_to_false(sender, **kwargs):
    Book.existing=False
    Book.save()

@receiver(post_delete,sender=Borrow)
def change_existing_book_to_True(sender, **kwargs):
    Book.existing=True
    Book.save()
