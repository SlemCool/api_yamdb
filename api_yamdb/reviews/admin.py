from django.contrib import admin

from .models import Category, Genre, Title, GenreTitle, Review, Comments

admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(GenreTitle)
admin.site.register(Review)
admin.site.register(Comments)
