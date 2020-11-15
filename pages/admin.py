from django.contrib import admin

from .models import Arm


class PostArm(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("name_arm", "id_arm", "dt_version_arm")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("name_arm",)
    # добавляем возможность фильтрации по дате
    list_filter = ("name_arm",)

admin.site.register(Arm, PostArm)
