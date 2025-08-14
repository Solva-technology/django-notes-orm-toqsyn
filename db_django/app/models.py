from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import max_length_name, max_length_text


class CustomUser(AbstractUser):
    name = models.CharField(max_length=max_length_name, db_index=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['name']

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<User id={self.id} name='{self.name}'>"


class UserProfile(models.Model):
    bio = models.TextField(max_length=max_length_text, blank=True)
    birth_date = models.DateField()
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='profile'
    )

    class Meta:
        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'профили пользователей'
        ordering = ['user__name']

    def __str__(self):
        return f'Профиль {self.user.name}'

    def __repr__(self):
        return f"<UserProfile id={self.id} user_id={self.user_id}>"


class Status(models.Model):
    name = models.CharField(max_length=max_length_name, unique=True)
    is_finalized = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'
        ordering = ['name']

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Status id={self.id} name='{self.name}'>"


class Category(models.Model):
    title = models.CharField(max_length=max_length_name, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Category id={self.id} title='{self.title}'>"


class Note(models.Model):
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='notes'
    )
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name='notes'
    )
    categories = models.ManyToManyField(Category, related_name='notes')

    class Meta:
        verbose_name = 'заметка'
        verbose_name_plural = 'заметки'
        ordering = ['-created_at']

    def __str__(self):
        return f'Заметка {self.id} от {self.author.name}'

    def __repr__(self):
        return f"<Note id={self.id} author_id={self.author_id}>"
