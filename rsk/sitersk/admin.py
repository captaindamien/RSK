from django import forms
from django.contrib import admin

from .models import Parent, Category, News
from ckeditor.widgets import CKEditorWidget


class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm


class CategoryAdmin(admin.ModelAdmin):
    form = NewsAdminForm


admin.site.register(News, NewsAdmin)
admin.site.register(Parent)
admin.site.register(Category, CategoryAdmin)
