# Generated by Django 3.2.4 on 2021-07-31 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0012_auto_20210730_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servertag',
            name='icon',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='servertag',
            name='name',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
    ]
