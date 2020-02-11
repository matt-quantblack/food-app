from django.contrib import admin
from .models import Profile
from .models import Recipe, Box

admin.site.register(Box)
admin.site.register(Profile)
admin.site.register(Recipe)
