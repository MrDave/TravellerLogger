from django.contrib import admin
from space_calendar.models import Campaign, GameDate, LogEntry


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    pass


@admin.register(GameDate)
class GameDateAdmin(admin.ModelAdmin):
    pass


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    pass
