# Generated by Django 4.1.6 on 2023-04-19 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medifindapp', '0004_delete_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='contact',
        ),
        migrations.DeleteModel(
            name='ActivityStatus',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='account',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='createdBy',
        ),
        migrations.DeleteModel(
            name='ContactSource',
        ),
        migrations.DeleteModel(
            name='ContactStatus',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]