from django.contrib import admin
from .models import Book,Author,Address,Country

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display=('name','code')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('city','pincode')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')
    

class BookAdmin(admin.ModelAdmin):
    list_display =('title','author') # by using this  table is created using title and author name in admin panel
    list_filter=('author','rating') # by using this filter is added in admin panel like flipkart,amzon site


admin.site.register(Country,CountryAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
