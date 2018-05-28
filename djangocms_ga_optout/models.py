# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class GAOptout(CMSPlugin):
    link_label = models.CharField(
        _('Link label'),
        max_length=511,
        help_text=_('Link text displayed to user'),
    )

    success_text = models.CharField(
        _('Success text'),
        max_length=511,
        blank=True,
        help_text=_('Text displayed when link is clicked. If empty, no alert will be shown.'),
    )

    class Meta:
        verbose_name = _('GA Optout')
        verbose_name_plural = _('GA Optouts')
