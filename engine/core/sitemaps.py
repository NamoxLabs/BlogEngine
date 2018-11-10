from django.conf import settings
from django.contrib.sitemaps import Sitemap

class I18Sitemap(Sitemap):
    protocol = 'https' if settings.ENABLE_SSL else 'http'
    i18n = True

class PageSitemap(I18nSitemap):

    def items(self):
        posts = Page.objects.public()
        return posts.only('id', 'title', 'slug')

sitemaps = {
    'pages': PageSitemap}