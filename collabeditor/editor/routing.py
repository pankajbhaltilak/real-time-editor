from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/doc/(?P<doc_id>\w+)/$', consumers.DocumentConsumer.as_asgi()),
]
