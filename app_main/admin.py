from django.contrib import admin
from .models import GameLevel

@admin.register(GameLevel)
class GameLevelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'difficulty', 'completed', 'stars']
    list_filter = ['difficulty', 'completed']
    search_fields = ['name', 'sentence']