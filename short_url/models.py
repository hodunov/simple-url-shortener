from django.db import models

from short_url.utils import create_shortened_url


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

    def save(self, *args, **kwargs):

        # If the short url wasn't specified
        if not self.short_url:
            # We pass the model instance that is being saved
            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)
