from smtplib import SMTP

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse
from rest_framework.authtoken.models import Token

from main.forms import RequestTokenEmailForm, ContactUsForm


def request_token(request):
    """Generates and emails API token for valid email address."""

    form = RequestTokenEmailForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        try:
            user = User.objects.get_by_natural_key(email)
        except ObjectDoesNotExist:
            user = User.objects.create_user(email)

        token = Token.objects.get_or_create(user=user)
        msg = 'Subject: %s\n\n%s' % ('NBA Authentication Token', 'Authentication Token: %s' % token[0].key)
        _send_email(email, msg)
        return HttpResponse('Success! Authentication token sent to: %s' % email)
    else:
        return HttpResponse('Error! Invalid email address')

def contact_us(request):
    """Emails user message for valid form."""

    form = ContactUsForm(request.POST)
    if form.is_valid():
        cleaned_form = form.cleaned_data
        subject = 'Subject: Contact Us\n\n%s%s%s'
        name = 'Name: %s\n' % cleaned_form['name']
        email = 'Email Address: %s\n' % cleaned_form['email']
        msg = 'Message: %s\n' % cleaned_form['message']
        ready_to_send = subject % (name, email, msg)

        _send_email(settings.NBA_APP_EMAIL, ready_to_send)
        return HttpResponse('Thank you for contacting us!')
    else:
        return HttpResponse('Error! Invalid data entered')

def _send_email(to_email, msg):
    """
    Sends email to application's email address with specified message.

    Args:
        msg (str): Message to include in email

    """
    username = settings.NBA_APP_EMAIL
    password = settings.NBA_APP_PASSWORD
    server = SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(username, to_email, msg)
    server.quit()
