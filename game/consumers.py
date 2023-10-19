import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Game


class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["game_id"]
        self.room_group_name = "game_%s" % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data_json = json.loads(text_data)
        response = await self.update_game_obj(data_json)
        # print('response', response)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_response',
                'data': response
            }
        )

    async def send_response(self, event):
        # print(event['data'])
        await self.send(text_data=json.dumps({'data': event['data']}))


    @database_sync_to_async
    def update_game_obj(self, data_json):
        game_id = self.scope["url_route"]["kwargs"]["game_id"]
        events = data_json['events']

        ball_position_x = events['ball_position']['x']
        ball_position_y = events['ball_position']['y']

        player_1_position_x = events['player_1_position']['x']
        player_1_position_y = events['player_1_position']['y']

        player_2_position_x = events['player_2_position']['x']
        player_2_position_y = events['player_2_position']['y']

        game_status = events['game_status']

        player_1_id = events['player_1']['id']
        player_1_name = events['player_1']['name']
        player_1_score = events['player_1']['score']

        player_2_id = events['player_2']['id']
        player_2_name = events['player_2']['name']
        player_2_score = events['player_2']['score']

        game_rule = events['game_rule']

        game_obj = Game.objects.get(pk=int(game_id))

        game_obj.ball_position_x = ball_position_x
        game_obj.ball_position_y = ball_position_y

        game_obj.player_1_position_x = player_1_position_x
        game_obj.player_1_position_y = player_1_position_y

        game_obj.player_2_position_x = player_2_position_x
        game_obj.player_2_position_y = player_2_position_y

        game_obj.game_status = game_status

        game_obj.player_1_id = player_1_id
        game_obj.player_1_name = player_1_name
        game_obj.player_1_score = player_1_score

        game_obj.player_2_id = player_2_id
        game_obj.player_2_name = player_2_name
        game_obj.player_2_score = player_2_score

        game_obj.game_rule = game_rule

        game_obj.save()

        response = {
            'id': game_id,
            'events': {
                'ball_position': {
                    'x': ball_position_x,
                    'y': ball_position_y,
                },
                'player_1_position': {
                    'x': player_1_position_x,
                    'y': player_1_position_y,
                },
                'player_2_position': {
                    'x': player_2_position_x,
                    'y': player_2_position_y,
                },
                'game_status': game_status,
                'player_1': {
                    'id': player_1_id,
                    'name': player_1_name,
                    'score': player_1_score,
                },
                'player_2': {
                    'id': player_2_id,
                    'name': player_2_name,
                    'score': player_2_score,
                },
                'game_rule': game_rule,
            }
        }
        return response

