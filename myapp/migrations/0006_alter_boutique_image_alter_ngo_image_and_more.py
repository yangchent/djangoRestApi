# Generated by Django 4.0.6 on 2022-08-03 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boutique',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
    ]
