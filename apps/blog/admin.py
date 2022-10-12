from django.contrib import admin
from .models import About, Tag, Comment, Category, History, How_it_works, Our_Team, Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')
    filter_horizontal = ('tag',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(About)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(History)
admin.site.register(How_it_works)
admin.site.register(Our_Team)