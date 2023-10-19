from django.db import models

# Create your models here.


class Game(models.Model):
	ball_position_x = models.IntegerField(null=True, blank=True)
	ball_position_y = models.IntegerField(null=True, blank=True)
	player_1_position_x = models.IntegerField(null=True, blank=True)
	player_1_position_y = models.IntegerField(null=True, blank=True)
	player_2_position_x = models.IntegerField(null=True, blank=True)
	player_2_position_y = models.IntegerField(null=True, blank=True)
	game_status = models.CharField(max_length=50, null=True, blank=True)
	player_1_id = models.IntegerField(null=True, blank=True)
	player_1_name = models.CharField(max_length=300, null=True, blank=True)
	player_1_score = models.IntegerField(null=True, blank=True)
	player_2_id = models.IntegerField(null=True, blank=True)
	player_2_name = models.CharField(max_length=300, null=True, blank=True)
	player_2_score = models.IntegerField(null=True, blank=True)
	game_rule = models.IntegerField(null=True, blank=True)
