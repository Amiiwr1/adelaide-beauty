from django.urls import reverse
from django.utils.decorators import method_decorator
from datetime import datetime
from django.views.decorators.cache import cache_control, cache_page
from django.views.generic import TemplateView
from django.conf import settings
from django.utils.translation import gettext_lazy as _


@method_decorator(cache_control(max_age=1 * 24 * 60 * 60), name='get')  # 1 day
@method_decorator(cache_page(1 * 24 * 60 * 60), name='get')  # 1 day
class HomePage(TemplateView):
    http_method_names = ['get']
    template_name = "home/index.html"
