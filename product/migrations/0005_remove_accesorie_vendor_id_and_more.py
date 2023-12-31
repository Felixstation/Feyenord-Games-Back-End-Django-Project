# Generated by Django 4.1.7 on 2023-05-13 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_accesoriesimage_accesorieimage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesorie',
            name='vendor_id',
        ),
        migrations.RemoveField(
            model_name='accesorieimage',
            name='accesories',
        ),
        migrations.RemoveField(
            model_name='console',
            name='vendor_id',
        ),
        migrations.RemoveField(
            model_name='consoleimage',
            name='console',
        ),
        migrations.RemoveField(
            model_name='game',
            name='vendor_id',
        ),
        migrations.DeleteModel(
            name='GameCategory',
        ),
        migrations.RemoveField(
            model_name='gameimage',
            name='game',
        ),
        migrations.RemoveField(
            model_name='vendorimage',
            name='vendor',
        ),
        migrations.DeleteModel(
            name='Accesorie',
        ),
        migrations.DeleteModel(
            name='AccesorieImage',
        ),
        migrations.DeleteModel(
            name='Console',
        ),
        migrations.DeleteModel(
            name='ConsoleImage',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='GameImage',
        ),
        migrations.DeleteModel(
            name='VendorImage',
        ),
    ]
