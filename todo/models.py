from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


@python_2_unicode_compatible
class List(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=100)
    last_mod = models.DateTimeField(verbose_name=_("last modification"), auto_now=True)
    creation_date = models.DateTimeField(verbose_name=_("creation date"), auto_now_add=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Item(MPTTModel):
    title = models.CharField(verbose_name=_("title"), max_length=100)
    content = models.TextField(verbose_name=_("content"), null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("author"), related_name='items')
    list = models.ForeignKey(List, verbose_name=_("list"), related_name='items', blank=True, null=True)
    parent = TreeForeignKey('self', verbose_name=_("parent"), related_name='children', null=True, blank=True)
    due_date = models.DateTimeField(verbose_name=_("due date"))
    done = models.BooleanField(verbose_name=_("done"), default=False)
    last_mod = models.DateTimeField(verbose_name=_("last modification"), auto_now=True)
    creation_date = models.DateTimeField(verbose_name=_("creation date"), auto_now_add=True)

    def __str__(self):
        return self.title
