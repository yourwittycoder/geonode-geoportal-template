from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse


class SustainLoginRequiredMiddleware:
    """
    Require browser users to authenticate while allowing
    authenticated API requests (including QGIS Basic Auth)
    to pass through without a browser login redirect.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Never redirect API requests.
        # GeoNode/QGIS authentication is handled by GeoNode's
        # API authentication middleware.
        if request.path.startswith("/api/"):
            return self.get_response(request)

        # Allow static/media assets.
        if request.path.startswith("/static/") or request.path.startswith("/media/"):
            return self.get_response(request)

        # Allow the login page itself.
        login_url = reverse("account_login")
        if request.path == login_url:
            return self.get_response(request)

        # Require authentication for normal web pages.
        if not request.user.is_authenticated:
            return HttpResponseRedirect(
                f"{login_url}?next={request.get_full_path()}"
            )

        return self.get_response(request)
