from django.db import models
from django.utils.timezone import now

from engine.account.models import User
from engine.category.models import Category, Subcategory
from engine.hashtag.models import Hashtag


class Post(models.Model):
    name = models.CharField(max_length=254, blank=False)
    content = models.TextField(blank=False)
    category = models.ForeignKey(Category, related_name='post_category',\
        null=True, editable=False, on_delete=models.SET_NULL)
    subcategories = models.ForeignKey(Subcategory, related_name='post_subcategory',\
        null=True, editable=False, on_delete=models.SET_NULL)
    hashtags = models.ManyToManyField(Hashtag, related_name='post_hashtags')
    created_by = models.ForeignKey(User, related_name='user_post',\
        null=True, editable=False, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=now, editable=False)
    changed = models.DateTimeField(default=now, editable=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at',)