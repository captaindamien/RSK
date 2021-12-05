from django.db import models
from django.utils import timezone


class Parent(models.Model):
    name = models.CharField(
        verbose_name='имя',
        max_length=150,
        unique=True,
    )
    link = models.CharField(
        verbose_name='Ссылка',
        max_length=50,
        default='index'
    )
    is_avaliable = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


class Category(models.Model):
    parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='имя',
        max_length=300,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class News(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='категория',
    )
    name = models.CharField(
        verbose_name='имя',
        max_length=300,
        unique=True,
    )
    short_desc = models.CharField(
        verbose_name='краткое описание',
        max_length=300,
        blank=True,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name='создано',
    )
    updated = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='обновлено',
    )
    download_counter = models.IntegerField(
        blank=True,
        default=0,
        verbose_name='кол-во скачиваний',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class UploadFile(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        verbose_name='Материал',
    )
    name = models.CharField(
        verbose_name='имя файла',
        max_length=300,
    )
    file = models.FileField(
        upload_to='files/',
        blank=True,
        verbose_name='Загрузить файл',
    )
    server_files = models.FilePathField(
        path='media/files/',
        blank=True,
        verbose_name='Выбрать файл на сервере',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Загрузка файла'
        verbose_name_plural = 'Загрузка файлов'
