from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import EmployeeImage, EmployeeSkill, Skill, User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Настройка отображения нашей кастомной модели User в админке."""

    # 1. Форма РЕДАКТИРОВАНИЯ существующего сотрудника
    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительная информация", {"fields": ("gender", "patronymic", "bio")}),
    )

    # 2. Форма СОЗДАНИЯ нового сотрудника
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "patronymic",
                    "gender",
                    "bio",
                ),
            },
        ),
    )

    # 3. Что показывать в общем списке сотрудников
    list_display = ("username", "last_name", "first_name", "gender", "is_staff")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(EmployeeSkill)
class EmployeeSkillAdmin(admin.ModelAdmin):
    list_display = ("employee", "skill", "level")
    list_filter = ("skill", "level")
    search_fields = ("employee__username", "employee__last_name", "skill__name")


# Регистрируем новую модель
@admin.register(EmployeeImage)
class EmployeeImageAdmin(admin.ModelAdmin):
    list_display = ("employee", "image", "order")
