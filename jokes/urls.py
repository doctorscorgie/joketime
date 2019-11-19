from django.urls import path
from . import views

urlpatterns = [
    path("", views.joke_index, name="joke_index"),
    path("<int:pk>/", views.joke_detail, name="joke_detail"),
    path("<category>/", views.joke_category, name="joke_category"),
]