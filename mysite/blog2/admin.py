from django.contrib import admin
from . import models
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_time')
    list_filter = ('pub_time',)###过滤器
admin.site.register(models.Article,ArticleAdmin)
