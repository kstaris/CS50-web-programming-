# Generated by Django 4.1 on 2022-09-06 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_listings_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listings',
            name='startBid',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listings',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
