# Generated by Django 4.1.7 on 2023-03-29 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.TextField(),
        ),
    ]