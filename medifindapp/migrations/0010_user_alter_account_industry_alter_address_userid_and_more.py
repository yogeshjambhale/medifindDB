# Generated by Django 4.1.6 on 2023-05-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medifindapp', '0009_remove_cartdata_file_remove_orders_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email ')),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='account',
            name='industry',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Industry Type'),
        ),
        migrations.AlterField(
            model_name='address',
            name='userId',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cartdata',
            name='userId',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='productId',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]