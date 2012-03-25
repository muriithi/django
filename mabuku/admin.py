from django.contrib import admin
from mabuku.models import Author , Book

class BookAdmin(admin.ModelAdmin):
	
	list_display = ('id','title', 'edition','isbn', 'purchase_date',)
	ordering = ('id',)


admin.site.register(Author)
admin.site.register(Book, BookAdmin)