from django.http import HttpResponse
from django.shortcuts import render

from .forms import GameForm
from .models import Game


def first_view(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

    context = {
        "form": GameForm(),
        "games": Game.objects.all()
    }

    return render(request, 'index.html', context)