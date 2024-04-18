# Generated by Django 5.0.4 on 2024-04-18 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customuser_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_image_1', models.ImageField(upload_to='product_images/')),
                ('product_image_2', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('product_image_3', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('product_image_4', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('product_image_5', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('description', models.TextField()),
                ('Colors', models.ManyToManyField(to='app.color')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('sizes', models.ManyToManyField(to='app.size')),
            ],
        ),
    ]