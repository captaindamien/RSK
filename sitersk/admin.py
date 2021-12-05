from django import forms
from django.contrib import admin

from .models import Parent, Category, News, UploadFile
from ckeditor.widgets import CKEditorWidget


class ParentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'pk',
        'link',
        'is_avaliable'
    )


class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = '__all__'
        verbose_name = 'Описание'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = (
        'name',
        'pk',
        'category',
        'created',
        'updated'
    )
    search_fields = (
        'name',
        'category__name',
    )


class UploadAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'news',
    )

    class Meta:
        model = UploadFile
        fields = '__all__'


admin.site.register(News, NewsAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Category)
admin.site.register(UploadFile, UploadAdmin)
