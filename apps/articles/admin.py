from django.contrib import admin

# Register your models here.
from .models import Article

admin.site.site_header = "TechAvoIA"
admin.site.site_title = "TechAvoIA"
admin.site.index_title = "Bem-vindo ao Portal de Administração"


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title','slug']
    list_display = ('title', 'date_added', 'public', 'likes', 'dislikes', 'ranking')
    list_editable = ('public',)
    list_filter = ('date_added', 'public')
    ordering = ('-date_added',)
    readonly_fields = ('views', 'likes', 'dislikes', 'ranking')
    filter_horizontal = ['related']
    save_on_top = True

admin.site.register(Article, ArticleAdmin)
