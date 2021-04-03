from django.contrib import admin
from person.models import *


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'fatherName']
