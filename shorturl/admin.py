from django.contrib import admin
from shorturl.models import urls
# Register your models here.
class urlsAdmin(admin.ModelAdmin):
    list_display = ('short_id','httpurl','pub_date', 'count')
    ordering = ('-pub_date',)
 
admin.site.register(urls, urlsAdmin) # Register the Urls model with UrlsAdmin options
