from django.contrib import admin
from .models import *

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    search_fields = ["name", ]
    list_display = ["id", "name", ]


class PlayerAdmin(admin.ModelAdmin):
    search_fields = ["first_name", "last_name", ]
    list_display = ["id", "first_name", "last_name", "team", ]


class TeamTableAdmin(admin.ModelAdmin):
    search_fields = ["name", ]

class ContactAdmin(admin.ModelAdmin):
    search_fields = ["name", "email"]

class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title",]

admin.site.register(Team, TeamAdmin)
admin.site.register(TeamTable, TeamTableAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Players, PlayerAdmin)

