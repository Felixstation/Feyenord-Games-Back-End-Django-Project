# Generated by Django 4.1.7 on 2023-07-19 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_product_created_at_product_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productversion',
            name='old_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]