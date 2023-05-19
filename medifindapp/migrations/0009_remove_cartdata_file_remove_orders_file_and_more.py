# Generated by Django 4.1.6 on 2023-04-22 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medifindapp', '0008_remove_products_file_products_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdata',
            name='file',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='file',
        ),
        migrations.AddField(
            model_name='cartdata',
            name='image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]