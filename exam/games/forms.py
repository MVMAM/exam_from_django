from django import forms

from .models import Game

class GameForm(forms.ModelForm):
    name_of_game = forms.CharField(max_length=255)
    author = forms.CharField(max_length=25)
    genre = forms.CharField(max_length=25)

    class Meta:
        model = Game
        fields = '__all__'