# Generated by Django 4.1.6 on 2023-05-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medifindapp', '0010_user_alter_account_industry_alter_address_userid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='userId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cartdata',
            name='productId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cartdata',
            name='userId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='productId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='userId',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
