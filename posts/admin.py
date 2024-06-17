from django.contrib import admin
from posts.models import Post, Tag, Advert, PostLike, PostComment, Alert
# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Advert)
admin.site.register(PostLike)
admin.site.register(PostComment)
admin.site.register(Alert) 
