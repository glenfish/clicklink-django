from django.http import HttpResponseForbidden

class CheckAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and not request.user.is_superuser:
            return HttpResponseForbidden("You are not authorized.")
        return self.get_response(request)

class CheckDeactivatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.is_deactivated:
            return HttpResponseForbidden("Your account is deactivated.")
        return self.get_response(request)
