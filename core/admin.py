from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "mobile", "course", "age", "created_by", "created_at")
    search_fields = ("full_name", "email", "mobile")
    list_filter = ("course", "created_at")
