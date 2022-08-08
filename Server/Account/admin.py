from django.contrib import admin
from .models import User, Team

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'team' ,'is_active', 'is_staff' )
    search_fields = ['username']
    list_filter = ['username', 'email', 'team','is_active', 'is_staff' ]
    ordering = ['id']

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']
    list_filter = ['name']
    ordering = ['id']

admin.site.register(User, UserAdmin)
admin.site.register(Team, TeamAdmin)

