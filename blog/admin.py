from django.contrib import admin

from blog.models import BlogPost
from blog.models import Tag


admin.site.register(BlogPost)

admin.site.register(Tag)



