# Generated by Django 3.0.7 on 2020-06-10 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favorites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritedeputado',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_deputados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favoriteproposicao',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_proposicoes', to=settings.AUTH_USER_MODEL),
        ),
    ]
