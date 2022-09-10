from django.contrib import admin

# Register your models here.

from .models import *



class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'copies','lang','summary')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

class InstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'due_back', 'status')

admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre)
admin.site.register(BookInstance,InstanceAdmin)
admin.site.register(Lang)
