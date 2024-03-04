from django.contrib import admin
from .models import user_data

# Register your models here.
class user_dataAdmin(admin.ModelAdmin):
    list_display = ('username', 'correo', 'celular', 'nit', 'password',)
    search_fields = ('username', 'correo', 'celular', 'nit', 'password',)
    list_filter = ('username', 'correo', 'celular', 'nit', 'password',)



admin.site.register(user_data, user_dataAdmin)