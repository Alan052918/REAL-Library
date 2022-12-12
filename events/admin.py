from django.contrib import admin

from .models import *

admin.site.register(Exhibition)
admin.site.register(ExhibitionUser)
admin.site.register(Seminar)
admin.site.register(Sponsor)
admin.site.register(SeminarSponsor)
admin.site.register(SeminarAuthor)
