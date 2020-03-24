from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Info)



class UserAdmin(admin.ModelAdmin):
    list_display = ['email']
    readonly_fields = ('password',)
    list_per_page = 50

admin.site.register(User, UserAdmin)