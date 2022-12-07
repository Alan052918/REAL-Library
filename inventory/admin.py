from django.contrib import admin

from .models import Topic, Book, Author, Copy, Rental, Invoice, Payment

admin.site.register(Topic)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Copy)
admin.site.register(Rental)
admin.site.register(Invoice)
admin.site.register(Payment)
