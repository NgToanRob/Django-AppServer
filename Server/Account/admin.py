from dataclasses import fields
from django.contrib import admin
from .models import User, Team

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    model= User
    list_display = ('id', 'username', 'team' ,'is_active', 'is_staff', 'is_superuser' )
    search_fields = ['username']
    list_filter = [ 'team' ,'is_active', 'is_staff' ]
    ordering = ['id']

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': [
                'team'
                ]
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('team')
        }),
    )

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']
    list_filter = ['name']
    ordering = ['id']


admin.site.register(Team, TeamAdmin)
admin.site.register(User, UserAdmin)
