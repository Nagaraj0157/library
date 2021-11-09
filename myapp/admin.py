from django.contrib import admin
from .models import Book,Admin
class booksdetails(admin.ModelAdmin):
    list_display=['Book_Name','isbn','Author','Language']
admin.site.register(Book,booksdetails)
class admindetails(admin.ModelAdmin):
    list_display=['name','email','password']
admin.site.register(Admin,admindetails)



