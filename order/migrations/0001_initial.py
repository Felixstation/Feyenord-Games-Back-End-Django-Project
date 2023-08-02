# Generated by Django 4.1.7 on 2023-05-21 12:24

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=60)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('address', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=15)),
            ],
        ),
    ]