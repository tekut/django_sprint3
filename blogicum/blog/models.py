from django.db import models
from django.contrib.auth import get_user_model


# Абстрактная модель
class BaseModel(models.Model):
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано'
                                       )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлено'
                                      )

    class Meta:
        abstract = True


# Публикация
class Post(BaseModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateField(verbose_name='Дата и время публикации')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор публикации'
                               )
    location = models.ForeignKey(Location,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 verbose_name='Местоположение'
                                 )
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Категория'
                                 )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'


# Тематическая категория
class Category(BaseModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=64,
                            unique=True,
                            verbose_name='Идентификатор')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


# Географическая метка
class Location(BaseModel):
    name = models.CharField(max_length=256, verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


# Пользователь
User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
