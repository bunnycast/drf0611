from django.contrib import admin

# Register your models here.
from cards.models import Cards


class CardsAdmin(admin.ModelAdmin):
    list_display = ['pk', ]


admin.site.register(Cards, CardsAdmin)
