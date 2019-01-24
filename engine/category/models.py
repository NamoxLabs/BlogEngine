from django.db import models
from django.utils.timezone import now

from engine.account.models import User


class Category(models.Model):
    name = models.CharField(max_length=254, blank=False, null=False, default='')
    description = models.TextField(blank=False, null=True, default='')
    created_by = models.ForeignKey(User, related_name='user_category',\
        null=True, editable=False, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=now, editable=False)
    changed = models.DateTimeField(default=now, editable=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at',)


class Subcategory(models.Model):
    name = models.CharField(max_length=254, blank=False, null=False, default='')
    description = models.TextField(blank=False, null=True, default='')
    category = models.ForeignKey(Category, related_name='category',\
        null=True, editable=False, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='user_subcategory',\
        null=True, editable=False, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=now, editable=True)
    changed = models.DateTimeField(default=now, editable=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at',)
