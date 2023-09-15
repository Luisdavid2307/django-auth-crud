from django.contrib import admin
from .models import Task

class taskadmin(admin.ModelAdmin):
    readonly_fields = ("created", )


admin.site.register(Task, taskadmin)

# Register your models here.
