from django.contrib import admin

from .models import Category,Post,Comment,Contact


# Register your models here.

class CateogoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)

   
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'post', 'author', 'content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author__username', 'post__title', 'content')

class ContactAdmin(admin.ModelAdmin):
    list_display= ('created_at','name','email','message')
    list_filter = ('created_at',)
    search_fields = ('email',)




admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Category,CateogoryAdmin)
admin.site.register(Post,PostAdmin)


