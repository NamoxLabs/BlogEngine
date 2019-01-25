from django.db import models
from django.utils.timezone import now

from engine.account.models import User


class BaseModel(models.Model):
    created_by = models.ForeignKey(User, null=True, editable=False, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=now, editable=False)
    changed = models.DateTimeField(default=now, editable=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at',)
