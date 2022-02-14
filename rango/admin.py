from django.contrib import admin
from rango.models import Category, Page 

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

# This is the register method to register the model 
admin.site.register(Page,PageAdmin)
admin.site.register(Category)

