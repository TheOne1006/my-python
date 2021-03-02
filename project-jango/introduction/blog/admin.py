from django.contrib import admin

# Register your models here.

from .models import Article


class AddressAdmin(admin.ModelAdmin):
    fields = ['address', 'pid']

admin.site.register(Article)