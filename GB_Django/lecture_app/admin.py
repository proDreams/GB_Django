from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Post)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.Author)
admin.site.register(models.UserModel)