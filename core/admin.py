from django.contrib import admin
from .models import Con


# Register your models here.
@admin.register(Con)
class contactadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message',)
