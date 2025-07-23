from django.db import models

from .constants import max_length_name, max_length_text


class User(models.Model):
    name = models.CharField(max_length=max_length_name)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    bio = models.TextField(max_length=max_length_text, blank=True, null=True)
    birth_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'профили пользователей'

    def __str__(self):
        return f'Профиль {self.user.name}'


class Status(models.Model):
    name = models.CharField(max_length=max_length_name, unique=True)
    is_final = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=max_length_name, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Note(models.Model):
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notes'
    )
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE
    )
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'заметка'
        verbose_name_plural = 'заметки'

    def __str__(self):
        return f'Заметка {self.id} от {self.author.name}'
