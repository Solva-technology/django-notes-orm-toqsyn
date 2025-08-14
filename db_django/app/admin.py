from django.contrib import admin

from .models import Category, CustomUser, Note, Status, UserProfile


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('is_active',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'birth_date')
    search_fields = ('user__name', 'user__email')
    autocomplete_fields = ('user',)
    ordering = ('birth_date',)
    list_filter = ('birth_date',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_finalized')
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'status', 'created_at')
    search_fields = ('text', 'author__name', 'author__email', 'status__name')
    list_filter = ('status', 'categories', 'created_at')
    autocomplete_fields = ('author', 'status', 'categories')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
