from datetime import timedelta

from django.utils import timezone
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from Model4.settings import TIME_TO_LIVE


class MyAuth(TokenAuthentication):
    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key=key)
        if (timezone.now() - token.created) > timedelta(minutes=TIME_TO_LIVE):
            raise exceptions.AuthenticationFailed("Token is invalid")
        token.created = timezone.now()
        token.save()
        return (token.user, token)
