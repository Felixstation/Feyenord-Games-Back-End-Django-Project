# Generated by Django 4.1.7 on 2023-05-17 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_productversion_platform_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productversion',
            name='platform_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='platform_id', to='product.platform', verbose_name='Platform'),
        ),
    ]
