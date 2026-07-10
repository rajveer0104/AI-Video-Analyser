from django.urls import path
from .views import chat
app_name = "rag"
urlpatterns = [
    path("chat/<int:transcript_id>/", chat, name="chat"),
]