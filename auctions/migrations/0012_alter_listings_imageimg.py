# Generated by Django 4.1 on 2022-09-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_rename_listing_id_bids_listing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='imageImg',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
