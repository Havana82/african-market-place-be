# Generated by Django 4.2.3 on 2023-08-04 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_api', '0005_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
