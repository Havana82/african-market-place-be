# Generated by Django 4.2.3 on 2023-07-25 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]