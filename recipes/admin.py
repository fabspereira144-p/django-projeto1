from django.contrib import admin

from .models import Category


class CategotyAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategotyAdmin)