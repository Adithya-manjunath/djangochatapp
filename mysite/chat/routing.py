from django.urls import re_path


from . import consumers


websocket_urlpatterns = [
    
    re_path(r'ws/chat/number/(?P<button_name>\w+)/$',consumers.ButtonClick.as_asgi()),
    re_path(r'ws/chat/coords/(?P<x>\w+)/get/(?P<y>\w+)/get/(?P<sx>\w+)/get/(?P<sy>\w+)/$',consumers.Coordinate.as_asgi()),
   
    re_path(r'ws/chat/(?P<room_name>\w+)/(?P<user_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    
]


