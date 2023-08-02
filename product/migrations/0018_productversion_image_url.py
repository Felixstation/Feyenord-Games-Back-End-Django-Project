# Generated by Django 4.1.7 on 2023-07-11 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_productversion_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='productversion',
            name='image_url',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_url', to='product.productimage', verbose_name='Image'),
        ),
    ]