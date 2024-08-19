from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail, EmailMessage

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
    
    
    
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # the below like concatinates your websites reset password url and the reset email token which will be required at a later stage
    email_plaintext_message = "Open the link to reset your password" + " " + "{}{}".format(instance.request.build_absolute_uri("http://localhost:4200/reset-password-form/"), reset_password_token.key)
    
    """
        this below line is the django default sending email function, 
        takes up some parameter (title(email title), message(email body), from(email sender), to(recipient(s))
    """
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Crediation portal account"),
        # message:
        email_plaintext_message,
        # from:
        "info@yourcompany.com",
        # to:
        [reset_password_token.user.email],
        fail_silently=False,
    )