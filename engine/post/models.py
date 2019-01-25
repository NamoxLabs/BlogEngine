from django.db import models
from django.utils.timezone import now

from engine.account.models import User
from engine.category.models import Category, Subcategory
from engine.hashtag.models import Hashtag

from engine.base_models.models import BaseModel


class Post(BaseModel):
    name = models.CharField(max_length=254, blank=False)
    content = models.TextField(blank=False)
    category = models.ForeignKey(Category, null=True, editable=False, on_delete=models.SET_NULL)
    subcategories = models.ManyToManyField(Subcategory)
    hashtags = models.ManyToManyField(Hashtag)
    
    class Meta:
        ordering = ('created_at',)
