from django.urls import path
from .views import analysis

app_name = "analysis"

urlpatterns = [
    path("<int:transcript_id>/", analysis, name="analysis"),
]