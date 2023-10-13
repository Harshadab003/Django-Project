from django.contrib import admin
from .models import Category,Toy, Accounts

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','cat_name']

class ToyAdmin(admin.ModelAdmin):
    list_display = ['id','toy_name','price','description','image','cat_fk']

class AccountsAdmin(admin.ModelAdmin):
    list_display = ['cardno','cvv','expiry','balance']

admin.site.register(Toy,ToyAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Accounts,AccountsAdmin)