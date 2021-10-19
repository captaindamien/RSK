from django.db import models


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
        max_length=150,
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
        max_length=100,
        unique=True,
    )
    short_desc = models.CharField(
        verbose_name='краткое описание продукта',
        max_length=150,
        blank=True,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name
