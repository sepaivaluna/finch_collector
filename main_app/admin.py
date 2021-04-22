from django.contrib import admin
from .models import Fan, FanAttire, Photo, World_Cup

# Register your models here.
admin.site.register(World_Cup)
admin.site.register(Fan)
admin.site.register(FanAttire)
admin.site.register(Photo)
