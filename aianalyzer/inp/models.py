from django.db import models


class Transcript(models.Model):

    title = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    transcript = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    summary = models.TextField(blank=True)

class Transcript(models.Model):
    title = models.CharField(max_length=255)
    transcript = models.TextField()
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title