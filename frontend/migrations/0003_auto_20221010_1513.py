# Generated by Django 3.2.16 on 2022-10-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20221006_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='images',
            name='thumbnail',
            field=models.CharField(default='none', max_length=250),
        ),
    ]
