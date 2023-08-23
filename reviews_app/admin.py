from django.contrib import admin

from reviews_app.models import Critique, Ticket
# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploader', 'image')


admin.site.register(Critique)
admin.site.register(Ticket, TicketAdmin)
