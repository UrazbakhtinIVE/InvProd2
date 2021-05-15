from django.contrib import admin

from mainapp.models import PeriodOfDiagnostics, Firm, Category
from .forms import AdminPeriodOfDiagnosticsForm


@admin.register(PeriodOfDiagnostics)
class PeriodOfDiagnosticsAdmin(admin.ModelAdmin):
    list_display = ("name", "period",)
    form = AdminPeriodOfDiagnosticsForm

@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
