# Generated by Django 2.1.4 on 2018-12-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]
