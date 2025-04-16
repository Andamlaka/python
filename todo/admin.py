from django.contrib import admin
from .models import TODO

@admin.register(TODO)
class TODOAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']  # Adjust fields if needed
