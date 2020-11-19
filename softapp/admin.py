from django.contrib import admin
from .models import UserQuery

# Register your models here.
class AdminMessage(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'number')
    list_display_links = ('id', 'name', 'email', 'number')
    list_filter = ('id', 'name', 'email', 'number')
    search_fields = ('id', 'name', 'email', 'number')
    list_per_page = 10

admin.site.register(UserQuery ,AdminMessage)
