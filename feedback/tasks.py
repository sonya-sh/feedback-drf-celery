from time import sleep

from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_feedback_email_task(email_address, message):
    
    sleep(10)  # Simulate expensive operation that freezes Django
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        "support@example.com",
        [email_address],
        fail_silently=False,
    )
