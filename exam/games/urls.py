from django.urls import path

from .views import *

urlpatterns = [
    path("", first_view, name="first_view"),
    path("details/<int:game_id>", game_details, name="game_details"),
    path("delete/<int:del_id>", delete_game, name="delete_game")
]