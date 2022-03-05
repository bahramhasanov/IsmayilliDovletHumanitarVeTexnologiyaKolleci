from datetime import datetime
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from celery import shared_task

from about.models import Event, Subscriber



@shared_task
def send_mail_to_subscribers():
    emails = Subscriber.objects.all().values_list('email',flat=True)
    events = Event.objects.filter(
        date__gte=datetime.now()).order_by('date')
    if emails and events:
        body = render_to_string('subscriber_email.html', context={
            'events':events,
        })
        msg = EmailMessage(subject=f'Kollecdən Müraciətlər {datetime.now().strftime("%d-%m-%Y")}', body=body,
                        from_email=settings.EMAIL_HOST_USER, to=emails, )
        msg.content_subtype = 'html'
        msg.send()


