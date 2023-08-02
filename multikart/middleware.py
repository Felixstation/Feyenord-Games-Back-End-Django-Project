from django.utils.deprecation import MiddlewareMixin
from core.models import BlockedIps

class SaveIpAdressMiddleware(MiddlewareMixin):
    def process_request(self , request):

        if request.user.is_authenticated:
            ip_address = request.META.get('REMOTE_ADDR')

            if not request.user.ips:
                request.user.ips = []

            if ip_address not in request.user.ips:
                request.user.ips.append(ip_address)

            return request.user.save()
        

class BlockIpAddress(MiddlewareMixin):
    def process_request(self , request):
        ip = request.META.get('REMOTE_ADDR')
        x = BlockedIps.objects.filter(ip_address = ip)

        if x:
            raise PermissionError('You are Blocked')
        


def force_default_language_middleware(get_response):
    """
        Ignore Accept-Language HTTP headers
        This will force the I18N machinery to always choose settings.LANGUAGE_CODE
        as the default initial language, unless another one is set via sessions or cookies
        Should be installed *before* any middleware that checks request.META['HTTP_ACCEPT_LANGUAGE'],
        namely django.middleware.locale.LocaleMiddleware
    """
    # One-time configuration and initialization.
    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if 'HTTP_ACCEPT_LANGUAGE' in request.META:
            del request.META['HTTP_ACCEPT_LANGUAGE']
        response = get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response
    return middleware