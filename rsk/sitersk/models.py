from django.db import models
from django.utils import timezone


class Parent(models.Model):
    name = models.CharField(
        verbose_name='имя',
        max_length=150,
        unique=True,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    def __str__(self):
        return self.name


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
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='имя',
        max_length=300,
        unique=True,
    )
    short_desc = models.CharField(
        verbose_name='краткое описание продукта',
        max_length=300,
        blank=True,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    files = models.FileField(
	upload_to='files/',
	blank=True,
    )
    created = models.DateTimeField(
        default=timezone.now,
    )
    updated = models.DateTimeField(
	blank=True,
	null=True,
    )
    download_counter = models.IntegerField(
	blank=True,
	default=0,
    )

    def __str__(self):
        return self.name
