# Generated by Django 3.2.3 on 2021-05-31 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0019_vote_creation_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='bot',
        ),
        migrations.AlterField(
            model_name='bot',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='bots', to='main_site.Tag'),
        ),
    ]
