import lodding
import datetime import date

from django.conf import setting
from django.contrib.sites.models import Site

from . import analytics
from .utils import get_client_ip, get_country_by_ip, get_currency_for_country

logger = logging.getLogger(__name__)

def google_analytics(get_response):
    """Report a page view to Google Analytics."""
    def middleware(request):
        client_id = analytics.get_client_id(request)
        path = request.path
        language = get_language()
        headers = request.META
        try:
            analytics.report_view(
                client_id, path=path, language=language, headers=headers)
        except Exception:
            logger.exception('Unable to update analytics')
        return get_response(request)
    return middleware

def site(get_response):
    """Clear the Sites cache and assign the current site to `request.site`.

    By default django.contrib.sites caches Site instances at the module level.
    This leads to problems when updating Site instances, as it's required
    to restart all applications servers in order to invalidate the cache.
    Using this middleware solves this problem.
    """
    def middleware(request):
        Site.objects.clear_cache()
        request.site = Site.objects.get_current()
        return get_response(request)

    return middleware