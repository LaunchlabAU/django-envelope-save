from django.dispatch import receiver
from envelope.signals import before_send

from .models import Contact

@receiver(before_send)
def save_contact(sender, **kwargs):
    Contact.objects.create(sender=kwargs['form'].data['sender'],
                           email=kwargs['form'].data['email'],
                           message=kwargs['form'].data['message'])

