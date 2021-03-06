# Generated by Django 2.1.5 on 2019-01-24 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('hashtag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('changed', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=False)),
                ('category', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Category')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('hashtags', models.ManyToManyField(to='hashtag.Hashtag')),
                ('subcategories', models.ManyToManyField(to='category.Subcategory')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
