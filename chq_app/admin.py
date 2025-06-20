from django.contrib import admin
from .models import master, order, replacement, new_order,boat_ticket
admin.site.register(master)
admin.site.register(order)
admin.site.register(replacement)
admin.site.register(new_order)
admin.site.register(boat_ticket)


# Register your models here.
class BookOption(admin.ModelAdmin):
    readonly_fields=['date']