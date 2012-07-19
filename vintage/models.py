from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic

from .settings import METADATA_FORM
from .compatible import ModelFormField
# from genericm2m.models import RelatedObjectsDescriptor


class ArchivedPage(models.Model):
    url = models.CharField(
        _('URL'),
        max_length=255,
        db_index=True,
        unique=True)
    title = models.CharField(
        _('title'),
        max_length=200)
    content = models.TextField(
        _('content'),
        blank=True)
    template_name = models.CharField(
        _('template name'),
        max_length=70,
        blank=True,
        help_text=_("""Example: 'vintage/contact_page.html'. If this
            isn't provided, the system will use 'vintage/default.html'."""))
    metadata = ModelFormField(METADATA_FORM)

    # related = RelatedObjectsDescriptor()

    class Meta:
        verbose_name = _('archived page')
        verbose_name_plural = _('archived pages')
        ordering = ('url',)

    def __unicode__(self):
        return "%s -- %s" % (self.url, self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('vintage_detail', (), {'url': self.url.lstrip('/')})
