# Generated by Django 4.1.7 on 2023-05-03 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('video', models.CharField(max_length=100)),
                ('vendor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='AccesoriesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product-images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('accesories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accesories_images', to='product.accesories')),
            ],
        ),
        migrations.CreateModel(
            name='Console',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('video', models.CharField(max_length=100)),
                ('vendor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='ConsoleImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product-images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('console', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='console_images', to='product.console')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
                ('about', models.TextField()),
                ('description', models.TextField()),
                ('video', models.CharField(max_length=100)),
                ('vendor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GameImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product-images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_images', to='product.game')),
            ],
        ),
        migrations.CreateModel(
            name='VendorImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='vendor-images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_images', to='product.vendor')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]