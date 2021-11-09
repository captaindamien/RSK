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
    list_display = ('name', 'category', 'created', 'updated')
#    fields = ['category', 'name', 'short_desc', 'description', 'created', 'updated']

#    def file_link(self, obj):
#	if obj.file:
#	    return "<a href='%s' download>Download</a>" % (obj.file.url,)
#	else:
#	    return "No attachment"
#    file_link.allow_tags = True
#    file_link.short_description = 'File Download'


class CategoryAdmin(admin.ModelAdmin):
    form = NewsAdminForm


admin.site.register(News, NewsAdmin)
admin.site.register(Parent)
admin.site.register(Category, CategoryAdmin)
