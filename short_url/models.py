from django.db import models


class Shortener(models.Model):
    """
    Creates a short url based on the long one
    created -> Hour and date a shortener was created
    times_followed -> Times the shortened link has been followed
    full_url -> The original link
    short_url ->  shortened link https://example/(short_url)
    """

    created_at = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    full_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_url} to {self.short_url}"
