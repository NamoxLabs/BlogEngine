from django.db import models
from django.utils import timezone

from engine.account.models import User


class Category(models.Model):
    name = models.CharField(max_length=254, blank=False, null=False, default='')
    description = models.TextField(blank=False, null=True, default='')
    created_by = models.ForeignKey(User, related_name='user_category',\
        null=True, editable=False, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now(), editable=True)
    changed = models.DateTimeField(default=timezone.now(), editable=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at',)


class Subcategory(models.Model):
    name = models.CharField(max_length=254, blank=False, null=False, default='')
    description = models.TextField(blank=False, null=True, default='')
    created_by = models.ForeignKey(User, related_name='user_subcategory',\
        null=True, editable=False, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now(), editable=True)
    changed = models.DateTimeField(default=timezone.now(), editable=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at',)
