from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Cards(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.SET_NULL,
                               null=True, verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name='Название проекта', blank=False)
    description = models.TextField(verbose_name='Описание проекта', blank=False)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    performers = models.ManyToManyField(MyUser, related_name='performers_card',
                                        blank=True, verbose_name='Исполнители')
    deadline = models.DateTimeField(verbose_name='Дедлайн', blank=False)
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата обновления карточки')
    archived = models.BooleanField(verbose_name='Добавить в архив', default=False, blank=True)

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True,
                               related_name='comment_author')
    card = models.ForeignKey(Cards, on_delete=models.CASCADE, related_name='comments_card')
    text = models.TextField(verbose_name='Поле для коментария')
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-created_time',)

    def __str__(self):
        return self.text
