# Generated by Django 3.2.3 on 2021-05-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0008_bot_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='banner_url',
            field=models.URLField(default='https://i.postimg.cc/15TN17rQ/xirprofilback.jpg'),
        ),
    ]
