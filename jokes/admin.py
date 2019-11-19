from django.contrib import admin

from django.contrib import admin
from jokes.models import Joke, JokeType


class JokeAdmin(admin.ModelAdmin):
    pass


class JokeTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Joke, JokeTypeAdmin)
admin.site.register(JokeType, JokeTypeAdmin)