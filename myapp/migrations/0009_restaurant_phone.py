# Generated by Django 4.0.6 on 2022-08-04 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_ngo_type_boutique_image_four_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(default='0000000000', max_length=15),
        ),
    ]
