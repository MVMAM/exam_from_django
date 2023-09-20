from .forms import GameForm
from .models import Game

def get_games_context():
    context = {
        'form': GameForm(),
        "users": Game.objects.all()
    }
    return context