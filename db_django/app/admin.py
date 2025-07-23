from django.contrib import admin

from .models import Category, Note, Status, User, UserProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'birth_date')
    search_fields = ('user__name', 'user__email')
    autocomplete_fields = ('user',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_final')
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
