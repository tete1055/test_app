from django.contrib import admin
from .models import CustomUser

#super user
# tenga
# tenga0114@icloud.com
# tenten14114

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    '''
    '''
    list_display = ('id', 'username')
    list_display_links = ('id', 'username')

admin.site.register(CustomUser, CustomUserAdmin)