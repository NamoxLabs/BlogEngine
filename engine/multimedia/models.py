from django.db import models
from django.utils.timezone import now

from engine.account.models import User
from engine.category.models import Category, Subcategory
from engine.hashtag.models import Hashtag
from engine.post.models import Post


class MultimediaUser(models.Model):
    name = models.CharField(max_length=254, blank=False)
    content = models.TextField(blank=False)
    user_related = models.ForeignKey(User, related_name='user_avatar',\
        null=True, editable=False, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name='user_multimedia_creator',\
        null=True, editable=False, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=now, editable=False)
    changed = models.DateTimeField(default=now, editable=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at',)


class MultimediaCategory(models.Model):
    name = models.CharField(max_length=254, blank=False)
    content = models.TextField(blank=False)
    category = models.ForeignKey(Category, related_name='multimedia_category',\
        null=True, editable=False, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name='user_multimedia_category',\
        null=True, editable=False, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=now, editable=False)
    changed = models.DateTimeField(default=now, editable=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at',)


class MultimediaSubategory(models.Model):
    name = models.CharField(max_length=254, blank=False)
    content = models.TextField(blank=False)
    subcategory = models.ForeignKey(Subcategory, related_name='multimedia_subcategory',\
        null=True, editable=False, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name='user_multimedia_subcategory',\
        null=True, editable=False, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=now, editable=False)
    changed = models.DateTimeField(default=now, editable=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at',)


class MultimediaPost(models.Model):
    name = models.CharField(max_length=254, blank=False)
    content = models.TextField(blank=False)
    post = models.ForeignKey(Post, related_name='multimedia_post',\
        null=True, editable=False, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name='user_multimedia_post',\
        null=True, editable=False, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=now, editable=False)
    changed = models.DateTimeField(default=now, editable=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at',)