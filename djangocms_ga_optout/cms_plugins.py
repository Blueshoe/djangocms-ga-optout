# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.translation import ugettext_lazy as _

from .models import GAOptout


class GAOptoutPlugin(CMSPluginBase):
    model = GAOptout
    name = _("Google Analytics Opt-Out")
    render_template = "djangocms_ga_optout/optout_link.html"
    text_enabled = True
    cache = True

    module = _('Google Analytics')

    def icon_src(self, instance):
        return static('djangocms_ga_optout/icons/ga.png')


plugin_pool.register_plugin(GAOptoutPlugin)
