# Generated by Django 4.1.7 on 2023-07-23 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='productversion',
            name='description_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='productversion',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='productversion',
            name='description_ru',
            field=models.TextField(null=True),
        ),
    ]