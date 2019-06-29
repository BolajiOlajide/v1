from django.contrib import admin
from django.contrib.auth.models import User

from blog_app.models import Post, Subscriber

# Register your models here.
class ProtonBlogAdminSite(admin.AdminSite):
    site_header = 'Proton\'s Blog Dashboard'


class PostAdminSite(admin.ModelAdmin):
    search_fields = ['id', 'title']
    exclude=('created_at', 'updated_at')


class SubscriberAdminSite(admin.ModelAdmin):
    search_fields = ['id', 'email']
    readonly_fields = ('email',)
    exclude=('created_at', 'updated_at')


class UserAdminSite(admin.ModelAdmin):
    search_fields = ['first_name', 'email', 'username']
    fields = ['username', 'first_name', 'email', 'is_staff', 'is_superuser']
    exclude = ('password',)


admin_site = ProtonBlogAdminSite(name='admin')
admin_site.register(Post, PostAdminSite)
admin_site.register(Subscriber, SubscriberAdminSite)
admin_site.register(User, UserAdminSite)
