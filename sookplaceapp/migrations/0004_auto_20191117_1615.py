# Generated by Django 2.2.7 on 2019-11-17 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sookplaceapp', '0003_sookplace_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sookplace',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
