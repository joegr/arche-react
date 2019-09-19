from django.contrib import admin
from .models import Deed # add this

class DeedAdmin(admin.ModelAdmin):  # add this
    list_display = ('title', 'detail', 'done') # add this

    # Register your models here.

admin.site.register(Deed, DeedAdmin) # add this
