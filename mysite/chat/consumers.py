import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_name=self.scope['url_route']['kwargs']['user_name']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
      
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': self.user_name+" : "+message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))


class ButtonClick(AsyncWebsocketConsumer):
    async def connect(self):
        self.button_name=self.scope['url_route']['kwargs']['button_name']
        self.room_group_name='chat_%s' % self.button_name
        print(self.room_group_name)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type":"chat_message",
                "message":self.button_name
            }
        )
        await self.accept()

    async def chat_message(self,event):
        message=event['message']

        await self.send(text_data=json.dumps({
            'message':message
        }))


class Coordinate(AsyncWebsocketConsumer):
    async def connect(self):
        self.x=self.scope['url_route']['kwargs']['x']
        self.y=self.scope['url_route']['kwargs']['y']
        self.sx=self.scope['url_route']['kwargs']['sx']
        self.sy=self.scope['url_route']['kwargs']['sy']
        self.room_group_name='chat_%s' % self.x

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type":"chat_message",
                "message":"client x: " + self.x+" client y: "+self.y+" screen x: "+self.sx+" screen y: "+self.sy
            }
        )
        await self.accept()

    async def chat_message(self,event):
        message=event['message']

        await self.send(text_data=json.dumps({
            'message':message
        }))

class Right(AsyncWebsocketConsumer):       
    async def connect(self):
        self.x=self.scope['url_route']['kwargs']['x']
        self.room_group_name='chat_%s' % self.x

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type":"chat_message",
                "message":"Right KEy press"
            }
        )
        await self.accept()

    async def chat_message(self,event):
        message=event['message']

        await self.send(text_data=json.dumps({
            'message':message
        }))

