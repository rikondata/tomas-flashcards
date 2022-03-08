# Generated by Django 3.2.9 on 2021-11-30 22:58

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
            name='deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deck', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='flashCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
                ('deck', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flashCard', to='flashcardsapp.deck')),
            ],
        ),
    ]