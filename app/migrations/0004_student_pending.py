# Generated by Django 3.1.5 on 2021-05-20 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210519_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='pending',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
