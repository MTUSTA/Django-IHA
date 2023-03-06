# Generated by Django 4.1.7 on 2023-03-05 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IhaApp', '0002_alter_iha_product_model_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='iha_product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iha_product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
