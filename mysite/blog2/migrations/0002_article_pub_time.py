# Generated by Django 2.0.7 on 2018-10-25 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
