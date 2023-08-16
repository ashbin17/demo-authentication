from django.contrib import admin
from rest_framework.authtoken.models import Token
from .models import User

# Register the Token model
admin.site.register(Token)
admin.site.register(User)
