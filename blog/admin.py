from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from blog.models import BlogPost


class BlogPostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BlogPost
        fields = ['pub_date', 'title', 'content']

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm

admin.site.register(BlogPost, BlogPostAdmin)