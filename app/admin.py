from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Product)