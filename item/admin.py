from django.contrib import admin
from .models import Category, Item
# Register your models here.
#allows us to register our models here that can then be managed in django's admin panel 
admin.site.register(Category)
admin.site.register(Item)
#admin.site.register()