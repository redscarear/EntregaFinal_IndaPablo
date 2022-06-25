# Generated by Django 4.0.5 on 2022-06-22 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('cuil', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tecnico_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
