from django.test import TestCase
from short_url.models import Shortener


class ShortenerTestCase(TestCase):
    def test_create_short_url(self):
        site_url = "https://example.com/"
        Shortener.objects.create(full_url=site_url)
        url_obj = Shortener.objects.first()
        short_url = url_obj.short_url
        full_url = url_obj.full_url
        self.assertNotEqual(site_url, short_url)
        self.assertEqual(site_url, full_url)
