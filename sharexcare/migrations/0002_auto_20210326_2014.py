# Generated by Django 3.1 on 2021-03-26 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharexcare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, max_length=900),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
