from django.shortcuts import render

from .forms import GameForm
from .models import Game
from .usecases import *


def first_view(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

    context = get_games_context()

    return render(request, 'index.html', context)

def game_details(request, game_id):
    game = Game.objects.get(id=game_id)
    context = {'game': game}
    return render(request, 'game_details.html', context)

def delete_game(request, del_id):
    game = Game.objects.get(id=del_id)
    print(game.name_of_game)
    game.delete()
    print(game.name_of_game)

    context = get_games_context()
    return render(request, 'index.html', context)