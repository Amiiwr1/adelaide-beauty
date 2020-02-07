from django.conf import settings


def adelaide_beauty(request):
    return {
        'settings': settings,
        'is_login': request.user.is_authenticated
    }
