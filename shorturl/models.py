from django.db import models

# Create your models here.
class urls(models.Model):
    short_id = models.SlugField(max_length=6,primary_key=True)
    httpurl = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.httpurl

    class Meta:
    	verbose_name_plural = 'urls'
