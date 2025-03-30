from django.contrib import admin
from .models import Users
# Register your models here.
class UserAdmin(admin .ModelAdmin):
  list_display=('login','password','limit','is_bloked')
admin.site.register(Users,UserAdmin)  