# Generated by Django 3.2.3 on 2021-05-28 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0007_auto_20210528_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='bots', to='main_site.Tag'),
        ),
    ]
