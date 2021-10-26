from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkManager(admin.ModelAdmin):
	list_display = ('link','author','short')
