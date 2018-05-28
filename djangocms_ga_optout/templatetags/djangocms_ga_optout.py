# -*- coding: utf-8 -*-

from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('djangocms_ga_optout/optout_js.html', takes_context=True)
def google_analytics_optout_js(context):
    return {'google_analytics_id': settings.GOOGLE_ANALYTICS_ID}
