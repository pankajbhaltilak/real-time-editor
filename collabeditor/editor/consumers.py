import json
from channels.generic.websocket import AsyncWebsocketConsumer

# In-memory store for users per document (reset on server restart)
active_users = {}

class DocumentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.doc_id = self.scope['url_route']['kwargs']['doc_id']
        self.room_group_name = f'document_{self.doc_id}'
        self.username = self.scope["user"].username

        # Track this user
        active_users.setdefault(self.room_group_name, set()).add(self.username)

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        # Broadcast updated active users list
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_list_update',
                'users': list(active_users[self.room_group_name])
            }
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

        # Remove user
        if self.room_group_name in active_users:
            active_users[self.room_group_name].discard(self.username)

            # Broadcast updated active users list
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'user_list_update',
                    'users': list(active_users[self.room_group_name])
                }
            )

    async def receive(self, text_data):
        # Broadcast the actual document content
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'document_message',
                'message': text_data
            }
        )

    async def document_message(self, event):
        await self.send(text_data=event['message'])

    async def user_list_update(self, event):
        await self.send(text_data=json.dumps({
            'type': 'users_update',
            'users': event['users']
        }))
