# Generated by Django 4.1.2 on 2022-10-25 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='slug',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
