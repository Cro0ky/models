# Generated by Django 4.2.6 on 2023-12-12 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
