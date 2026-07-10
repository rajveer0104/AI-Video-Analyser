from django.urls import path
from .views import summarize

app_name = "summary"

urlpatterns = [
    path("<int:transcript_id>/", summarize, name="summarize"),
]