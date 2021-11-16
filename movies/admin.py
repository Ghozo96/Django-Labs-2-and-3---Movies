from django.contrib import admin
from .models import Movie, Actor, Review

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'watch_count', 'likes', 'creation_date')
    list_display_links = ('name',)
    search_fields = ('name', 'description')

    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review', 'movie', 'creation_date')
    list_display_links = ('review',)
    list_filter = ('movie',)



admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)
admin.site.register(Review, ReviewAdmin)