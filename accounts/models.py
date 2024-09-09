from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail, EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class CustomUser(AbstractUser):
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return({
            'refresh': str(refresh),
            'refresh': str(refresh.access_token),
        })
        
    # def validate_password(self, value: str) -> str:
    #     """
    #     Hash value passed by user.

    #     :param value: password of a user
    #     :return: a hashed version of the password
    #     """
    #     return make_password(value)
    
    
    
# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

#     # the below like concatinates your websites reset password url and the reset email token which will be required at a later stage
#     email_plaintext_message = "Open the link to reset your password" + " " + "{}{}".format(instance.request.build_absolute_uri("http://localhost:4200/reset-password-form/"), reset_password_token.key)
    
#     """
#         this below line is the django default sending email function, 
#         takes up some parameter (title(email title), message(email body), from(email sender), to(recipient(s))
#     """
#     send_mail(
#         # title:
#         "Password Reset for {title}".format(title="Crediation portal account"),
#         # message:
#         email_plaintext_message,
#         # from:
#         "info@yourcompany.com",
#         # to:
#         [reset_password_token.user.email],
#         fail_silently=False,
#     )
    
    
    
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # Baue den Reset-Link
    reset_link = "{}{}".format(instance.request.build_absolute_uri("https://videoflix.regina-gering.com/reset-password-form/"), reset_password_token.key)

    # Render das HTML-Template mit den Variablen
    email_html_message = render_to_string('reset_password.html', {
        'reset_link': reset_link,
    })

    # Falls notwendig, den Text-Inhalt der E-Mail strippen (für den plain text fallback)
    email_plaintext_message = strip_tags(email_html_message)

    # Erstelle die E-Mail
    email = EmailMultiAlternatives(
        # Betreff
        "Password Reset for {title}".format(title="Crediation portal account"),
        # Plain-Text-Nachricht (für Clients, die kein HTML unterstützen)
        email_plaintext_message,
        # Absender
        "info@videoflix.com",
        # Empfänger
        [reset_password_token.user.email]
    )

    # Füge den HTML-Inhalt hinzu
    email.attach_alternative(email_html_message, "text/html")

    # Sende die E-Mail
    email.send()

