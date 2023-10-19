from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Game


@require_http_methods(["GET", "POST"])
def create_game(request):
	game = Game.objects.create()
	response = {
		'message': 'Game Created Successfully',
		'success': True,
		'status': 200,
		'data': {'game_id': game.pk}
	}
	return JsonResponse(response)

def join_game(request):
	return render(request, 'game/join_game.html')

def play_game(request, game_id):
	return render(request, 'game/play_game.html', {'game_id': game_id})