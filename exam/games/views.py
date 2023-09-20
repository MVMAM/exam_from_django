from django.http import HttpResponse
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

def game_details(request, user_id):
    user = Game.objects.get(id=user_id)
    context = {'user': user}
    return render(request, 'game_details.html', context)

def delete_game(request, del_id):
    user = Game.objects.get(id=del_id)
    print(user.first_name)
    user.delete()
    print(user.first_name)

    context = get_games_context()
    return render(request, 'index.html', context)