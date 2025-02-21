from django.contrib import admin

from main.models import People, Rank


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    pass


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    pass
