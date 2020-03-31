from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from reservation.models import Order


@receiver(post_save, sender=Order)
def send_mail_signal(sender, **kwargs):
    if kwargs['created']:
        instance = kwargs['instance']
        send_mail(
            'Thank for registration',
            'Thank for registration',
            instance.email,
            ['to@example.com'],
            fail_silently=False,
        )
