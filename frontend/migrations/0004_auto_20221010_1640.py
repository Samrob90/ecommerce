# Generated by Django 3.2.16 on 2022-10-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_auto_20221010_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='products',
        ),
        migrations.AddField(
            model_name='products',
            name='images',
            field=models.ManyToManyField(default=None, to='frontend.images'),
        ),
    ]
