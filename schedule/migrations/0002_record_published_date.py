# Generated by Django 2.0.13 on 2019-04-20 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]