# Generated by Django 4.1.7 on 2023-05-13 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ProductImage',
        ),
    ]