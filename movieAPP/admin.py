from django.contrib import admin
from movieAPP.models import Review, StreamPlatform, WatchList

admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)
