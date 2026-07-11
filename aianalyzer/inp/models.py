from django.db import models


class Transcript(models.Model):
    title = models.CharField(max_length=255)

    transcript = models.TextField()

    summary = models.TextField(blank=True, null=True)

    segments = models.JSONField(default=list)

    created_at = models.DateTimeField(auto_now_add=True)

    video_path = models.CharField(max_length=500, blank=True, null=True)

    youtube_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title