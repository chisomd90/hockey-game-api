from django.urls import path
from .views import create_game, join_game, play_game


urlpatterns = [
	path('game-create/', create_game, name='create_game'),
	path('join-game/', join_game, name='join_game'),
	path('play-game/<int:game_id>/', play_game, name='play_game'),
]