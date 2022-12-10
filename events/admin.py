from django.contrib import admin

from .models import Exhibition, Seminar, Sponsor, SeminarSponsor, SeminarAuthor

admin.site.register(Exhibition)
admin.site.register(Seminar)
admin.site.register(Sponsor)
admin.site.register(SeminarSponsor)
admin.site.register(SeminarAuthor)
